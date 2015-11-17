# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151023_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='producer',
            field=models.TextField(null=True, blank=True),
        ),
    ]
