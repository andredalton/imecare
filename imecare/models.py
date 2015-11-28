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
    ('A-', 'A-  .'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-.'),
    ('B+', 'B+'),
    ('B-', 'B-.'),
    ('O+', 'O+'),
    ('O-', 'O-.')
)

class Telefone(models.Model):
    numero = models.CharField(max_length=100, verbose_name='Número')
    contato = models.CharField(max_length=150, verbose_name='Nome do contato')
    parentesco = models.CharField(max_length=50)

    class Meta:
        unique_together = ('numero', 'contato', 'parentesco')

class Paciente(User):
    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=50, verbose_name='RG', unique=True)
    cpf = models.CharField(max_length=50, verbose_name='CPF', unique=True)
    tipo_sanguineo = models.CharField(max_length=2, choices=SANGUE_CHOICES, verbose_name='Tipo sanguíneo')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    telefones = models.ManyToManyField(Telefone)

    def save(self):
        # Tornando o nome de usuário User igual ao cpf
        self.username = self.cpf
        if verifica_cpf(self.cpf):
            return super(Paciente, self).save()

class Medico(User):
    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=50, verbose_name='RG', unique=True)
    cpf = models.CharField(max_length=50, verbose_name='CPF', unique=True)
    crm = models.CharField(max_length=50, verbose_name='CRM', unique=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    telefones = models.ManyToManyField(Telefone)

    def save(self):
        # Tornando o nome de usuário User igual ao crm e is_staff = True
        self.username = self.cpf
        if verifica_cpf(self.cpf):
            return super(Medico, self).save()
