# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151023_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='birth_year',
            field=models.TextField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='height',
            field=models.TextField(null=True, blank=True),
        ),
    ]
