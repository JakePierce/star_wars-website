# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20151023_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='climate',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='gravity',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='terrain',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
