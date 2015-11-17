# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151023_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='height',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
