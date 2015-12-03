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
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentarios', models.TextField(verbose_name=b'coment\xc3\xa1rios', blank=True)),
                ('data', models.DateField(auto_now=True)),
                ('horario', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosticada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cronica', models.BooleanField(default=False, verbose_name=b'cr\xc3\xb4nica')),
                ('inicio', models.DateField(auto_now=True)),
                ('fim', models.DateField(default=None, null=True)),
                ('atendimento', models.ForeignKey(to='imecare.Atendimento')),
            ],
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('nome', models.CharField(unique=True, max_length=150)),
                ('cid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('generica', models.ForeignKey(to='imecare.Doenca', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=150)),
                ('rg', models.CharField(unique=True, max_length=15, verbose_name=b'RG')),
                ('cpf', models.CharField(unique=True, max_length=15, verbose_name=b'CPF')),
                ('crm', models.CharField(max_length=15, unique=True, null=True, verbose_name=b'CRM', blank=True)),
                ('tipo_sanguineo', models.CharField(max_length=3, verbose_name=b'Tipo sangu\xc3\xadneo', choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'O+', b'O+'), (b'O-', b'O-')])),
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
            name='Procedimento',
            fields=[
                ('nome', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solicita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalhes', models.TextField(blank=True)),
                ('atendimento', models.ForeignKey(to='imecare.Atendimento')),
                ('procedimento', models.ForeignKey(to='imecare.Procedimento')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosticada',
            name='doenca',
            field=models.ForeignKey(to='imecare.Doenca'),
        ),
        migrations.AddField(
            model_name='diagnosticada',
            name='paciente',
            field=models.ForeignKey(to='imecare.Pessoa'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='medico',
            field=models.ForeignKey(related_name='medico', to='imecare.Pessoa'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(related_name='paciente', to='imecare.Pessoa'),
        ),
        migrations.AlterUniqueTogether(
            name='atendimento',
            unique_together=set([('medico', 'paciente', 'data', 'horario')]),
        ),
    ]
