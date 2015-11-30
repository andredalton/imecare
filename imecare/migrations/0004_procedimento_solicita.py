# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0003_atendimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
                ('nome', models.CharField(max_length=100)),
                ('cod_anvisa', models.PositiveIntegerField(verbose_name=b'c\xc3\xb3digo anvisa')),
            ],
        ),
        migrations.CreateModel(
            name='Solicita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atendimento', models.OneToOneField(to='imecare.Atendimento')),
                ('procedimento', models.OneToOneField(to='imecare.Procedimento')),
            ],
        ),
    ]
