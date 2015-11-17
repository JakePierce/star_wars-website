# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20151102_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='starships_url',
            field=models.TextField(null=True, blank=True),
        ),
    ]
