# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20151026_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
