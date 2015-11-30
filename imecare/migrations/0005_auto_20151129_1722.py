# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0004_procedimento_solicita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedimento',
            name='id',
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='cod_anvisa',
            field=models.PositiveIntegerField(serialize=False, verbose_name=b'c\xc3\xb3digo anvisa', primary_key=True),
        ),
    ]
