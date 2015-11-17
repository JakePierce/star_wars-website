# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20151026_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='average_height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='average_lifespan',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
