#!/usr/bin/python
# -*- coding: UTF8 -*-

import re
from django.db import models
from django.contrib.auth.models import User


def verifica_cpf(cpf):
    m = re.search("([0-9]{3})\.([0-9]{3})\.([0-9]{3})-([0-9]{2})", cpf)
    corpo = map(int, list(m.group(1) + m.group(2) + m.group(3)))
    digito = map(int, list(m.group(4)))
    mult = zip(corpo, range(10, 1, -1))
    soma = sum(map(lambda tup: tup[0]*tup[1], mult))

    if ((10*soma) % 11) % 10 == digito[0]:
        mult = zip(corpo + [digito[0]], range(11, 1, -1))
        soma = sum(map(lambda tup: tup[0]*tup[1], mult))
        if ((10*soma) % 11) % 10 == digito[1]:
            return True
    return False

SANGUE_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-')
)


class Pessoa(User):
    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=15, verbose_name='RG', unique=True)
    cpf = models.CharField(max_length=15, verbose_name='CPF', unique=True)
    crm = models.CharField(max_length=15, verbose_name='CRM', unique=True, null=True, blank=True)
    tipo_sanguineo = models.CharField(max_length=3, choices=SANGUE_CHOICES, verbose_name='Tipo sanguíneo')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')

    def save(self):
        # Tornando o nome de usuário User igual ao cpf
        self.username = self.cpf
        if verifica_cpf(self.cpf):
            return super(Pessoa, self).save()


class Atendimento(models.Model):
    medico = models.ForeignKey(Pessoa, related_name='medico')
    paciente = models.ForeignKey(Pessoa, related_name='paciente')
    comentarios = models.TextField(verbose_name='comentários')
    data = models.DateField(auto_now=True)
    horario = models.TimeField(auto_now=True)

    class Meta:
        unique_together = (("medico", "paciente", "data", "horario"),)

    def save(self):
        if self.medico.is_staff:
            return super(Atendimento, self).save()


class Procedimento(models.Model):
    descricao = models.TextField(verbose_name='descrição')
    nome = models.CharField(max_length=100, primary_key=True)


class Solicita(models.Model):
    procedimento = models.ForeignKey(Procedimento)
    atendimento = models.ForeignKey(Atendimento)
    detalhes = models.TextField(blank=True)
