# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20151026_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='model',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
