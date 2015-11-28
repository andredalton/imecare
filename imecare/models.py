#!/usr/bin/python
# -*- coding: UTF8 -*-

from django.db import models
from django.contrib.auth.models import User

SANGUE_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-.'),
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
        return super(Paciente, self).save()