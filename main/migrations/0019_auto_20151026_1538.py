# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20151026_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='films',
            field=models.ManyToManyField(to='main.Film', blank=True),
        ),
    ]
