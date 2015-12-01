# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0012_auto_20151130_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosticada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticadaEm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cronica', models.BooleanField(default=False)),
                ('inicio', models.DateField(auto_now=True)),
                ('fim', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='comentarios',
            field=models.TextField(verbose_name=b'coment\xc3\xa1rios', blank=True),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='generica',
            field=models.ForeignKey(to='imecare.Doenca', null=True),
        ),
        migrations.AddField(
            model_name='diagnosticadaem',
            name='doenca',
            field=models.ForeignKey(to='imecare.Doenca'),
        ),
        migrations.AddField(
            model_name='diagnosticadaem',
            name='paciente',
            field=models.ForeignKey(to='imecare.Pessoa'),
        ),
        migrations.AddField(
            model_name='diagnosticada',
            name='atendimento',
            field=models.ForeignKey(to='imecare.Atendimento'),
        ),
        migrations.AddField(
            model_name='diagnosticada',
            name='doenca',
            field=models.ForeignKey(to='imecare.Doenca'),
        ),
    ]
