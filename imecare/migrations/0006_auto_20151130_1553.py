# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0005_auto_20151129_1722'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='atendimento',
            unique_together=set([('medico', 'paciente', 'data', 'horario')]),
        ),
    ]
