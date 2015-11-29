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
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=150)),
                ('rg', models.CharField(unique=True, max_length=15, verbose_name=b'RG')),
                ('cpf', models.CharField(unique=True, max_length=15, verbose_name=b'CPF')),
                ('crm', models.CharField(max_length=15, unique=True, null=True, verbose_name=b'CRM', blank=True)),
                ('tipo_sanguineo', models.CharField(max_length=2, verbose_name=b'Tipo sangu\xc3\xadneo', choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'O+', b'O+'), (b'O-', b'O-')])),
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
    ]
