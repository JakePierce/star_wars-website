# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20151026_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='classification',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='designation',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
