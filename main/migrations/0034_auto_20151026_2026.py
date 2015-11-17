# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20151026_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='cost_in_credits',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='max_atmosphering_speed',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
