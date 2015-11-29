# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0002_auto_20151129_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentarios', models.TextField(verbose_name=b'coment\xc3\xa1rios')),
                ('data', models.DateField(auto_now=True)),
                ('horario', models.TimeField(auto_now=True)),
                ('medico', models.OneToOneField(related_name='medico', to='imecare.Pessoa')),
                ('paciente', models.OneToOneField(related_name='paciente', to='imecare.Pessoa')),
            ],
        ),
    ]
