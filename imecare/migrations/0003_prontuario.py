# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0002_realiza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=20)),
                ('texto', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('medico', models.ForeignKey(related_name='+', to='imecare.Pessoa', null=True)),
                ('paciente', models.ForeignKey(related_name='+', to='imecare.Pessoa')),
            ],
        ),
    ]
