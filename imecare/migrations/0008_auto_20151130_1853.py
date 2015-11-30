# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0007_auto_20151130_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimento',
            name='nome',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='solicita',
            name='atendimento',
            field=models.ForeignKey(to='imecare.Atendimento'),
        ),
        migrations.AlterField(
            model_name='solicita',
            name='procedimento',
            field=models.ForeignKey(to='imecare.Procedimento'),
        ),
    ]
