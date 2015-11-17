# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20151026_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='consumables',
            field=models.TextField(null=True, blank=True),
        ),
    ]
