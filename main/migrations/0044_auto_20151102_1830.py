# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20151102_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='planets_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='species_url',
            field=models.TextField(null=True, blank=True),
        ),
    ]
