# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('imecare', '0002_auto_20151128_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=150)),
                ('rg', models.CharField(unique=True, max_length=50, verbose_name=b'RG')),
                ('cpf', models.CharField(unique=True, max_length=50, verbose_name=b'CPF')),
                ('crm', models.CharField(unique=True, max_length=50, verbose_name=b'CRM')),
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
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sanguineo',
            field=models.CharField(max_length=2, verbose_name=b'Tipo sangu\xc3\xadneo', choices=[(b'A+', b'A+'), (b'A-', b'A-  .'), (b'AB+', b'AB+'), (b'AB-', b'AB-.'), (b'B+', b'B+'), (b'B-', b'B-.'), (b'O+', b'O+'), (b'O-', b'O-.')]),
        ),
        migrations.AlterUniqueTogether(
            name='telefone',
            unique_together=set([('numero', 'contato', 'parentesco')]),
        ),
        migrations.AddField(
            model_name='medico',
            name='telefones',
            field=models.ManyToManyField(to='imecare.Telefone'),
        ),
    ]
