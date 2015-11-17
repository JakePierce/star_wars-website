# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151023_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='population',
            field=models.TextField(null=True, blank=True),
        ),
    ]
