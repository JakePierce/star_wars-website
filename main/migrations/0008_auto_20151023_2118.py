# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151023_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='mass',
            field=models.TextField(null=True, blank=True),
        ),
    ]
