# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20151023_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='MGLT',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cargo_capacity',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cost_in_credits',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='crew',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='length',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='manufacturer',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='max_atmosphering_speed',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
