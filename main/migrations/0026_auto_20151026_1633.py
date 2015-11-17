# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20151026_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='people',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
