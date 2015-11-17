# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20151026_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='language',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
