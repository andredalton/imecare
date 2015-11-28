# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=150)),
                ('rg', models.CharField(max_length=50, verbose_name=b'RG')),
                ('cpf', models.CharField(max_length=50, verbose_name=b'CPF')),
                ('tipo_sanguineo', models.CharField(max_length=2, verbose_name=b'Tipo sangu\xc3\xadneo', choices=[(b'A+', b'A+'), (b'A-', b'A-.'), (b'AB+', b'AB+'), (b'AB-', b'AB-.'), (b'B+', b'B+'), (b'B-', b'B-.'), (b'O+', b'O+'), (b'O-', b'O-.')])),
                ('data_nascimento', models.DateField(verbose_name=b'Data de nascimento')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=100, verbose_name=b'N\xc3\xbamero')),
                ('contato', models.CharField(max_length=150, verbose_name=b'Nome do contato')),
                ('parentesco', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefones',
            field=models.ManyToManyField(to='imecare.Telefone'),
        ),
    ]
