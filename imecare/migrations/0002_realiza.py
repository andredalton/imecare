# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realiza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(auto_now=True)),
                ('horario', models.TimeField(auto_now=True)),
                ('paciente', models.ForeignKey(to='imecare.Pessoa')),
                ('procedimento', models.ForeignKey(to='imecare.Procedimento')),
                ('solicitacao', models.ForeignKey(default=None, to='imecare.Solicita', null=True)),
            ],
        ),
    ]
