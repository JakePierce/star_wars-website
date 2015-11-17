# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151023_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='orbital_period',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='rotation_period',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
