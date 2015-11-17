# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20151030_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='vehicles',
        ),
        migrations.AddField(
            model_name='people',
            name='vehicles',
            field=models.ManyToManyField(related_name='the_vehicles', to='main.Vehicles', blank=True),
        ),
    ]
