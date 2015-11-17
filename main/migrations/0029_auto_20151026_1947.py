# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20151026_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='average_lifespan',
            field=models.TextField(null=True, blank=True),
        ),
    ]
