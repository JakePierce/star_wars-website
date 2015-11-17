# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20151026_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='MGLT',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cargo_capacity',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cost_in_credits',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='crew',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='hyperdrive_rating',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='length',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='max_atmosphering_speed',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.TextField(null=True, blank=True),
        ),
    ]
