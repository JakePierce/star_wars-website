# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151023_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='opening_crawl',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.TextField(null=True, blank=True),
        ),
    ]
