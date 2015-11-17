# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20151030_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='homeworld',
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ManyToManyField(to='main.Planet', blank=True),
        ),
    ]
