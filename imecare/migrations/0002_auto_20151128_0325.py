# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'CPF'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rg',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'RG'),
        ),
    ]
