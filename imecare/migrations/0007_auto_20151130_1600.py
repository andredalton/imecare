# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0006_auto_20151130_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='medico',
            field=models.ForeignKey(related_name='medico', to='imecare.Pessoa'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(related_name='paciente', to='imecare.Pessoa'),
        ),
    ]
