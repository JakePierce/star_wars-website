# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20151102_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='vehicles_url',
            field=models.TextField(null=True, blank=True),
        ),
    ]
