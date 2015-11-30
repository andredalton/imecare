# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0008_auto_20151130_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedimento',
            name='cod_anvisa',
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='nome',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
