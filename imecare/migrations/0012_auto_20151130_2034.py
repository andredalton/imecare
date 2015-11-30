# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0011_doenca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doenca',
            name='generica',
            field=models.ForeignKey(blank=True, to='imecare.Doenca', null=True),
        ),
    ]
