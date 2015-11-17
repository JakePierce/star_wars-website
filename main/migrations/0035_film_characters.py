# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20151026_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='characters',
            field=models.URLField(null=True, blank=True),
        ),
    ]
