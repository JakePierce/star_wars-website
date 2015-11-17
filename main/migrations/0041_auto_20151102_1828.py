# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20151102_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='species_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='characters_url',
            field=models.TextField(null=True, blank=True),
        ),
    ]
