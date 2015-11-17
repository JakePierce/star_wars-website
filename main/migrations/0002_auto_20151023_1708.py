# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='cost_in_credits',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
