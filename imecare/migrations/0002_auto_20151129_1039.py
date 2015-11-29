# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imecare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='tipo_sanguineo',
            field=models.CharField(max_length=3, verbose_name=b'Tipo sangu\xc3\xadneo', choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'O+', b'O+'), (b'O-', b'O-')]),
        ),
    ]
