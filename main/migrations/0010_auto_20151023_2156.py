# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151023_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='residents',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
