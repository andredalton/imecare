# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0009_auto_20151130_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicita',
            name='detalhes',
            field=models.TextField(blank=True),
        ),
    ]
