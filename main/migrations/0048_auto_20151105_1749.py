# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20151102_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='people',
        ),
        migrations.AddField(
            model_name='people',
            name='species',
            field=models.ManyToManyField(related_name='the_species', to='main.Species', blank=True),
        ),
    ]
