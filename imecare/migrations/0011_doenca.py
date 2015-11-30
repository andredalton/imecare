# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0010_solicita_detalhes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('nome', models.CharField(unique=True, max_length=150)),
                ('cid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('generica', models.ForeignKey(to='imecare.Doenca')),
            ],
        ),
    ]
