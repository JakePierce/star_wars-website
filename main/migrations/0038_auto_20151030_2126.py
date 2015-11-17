# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20151030_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='species',
        ),
        migrations.AddField(
            model_name='people',
            name='species',
            field=models.ManyToManyField(related_name='the_species', to='main.Species', blank=True),
        ),
    ]
