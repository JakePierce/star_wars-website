# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20151102_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='species',
        ),
        migrations.RemoveField(
            model_name='species',
            name='people',
        ),
        migrations.AddField(
            model_name='species',
            name='people',
            field=models.ManyToManyField(to='main.People', blank=True),
        ),
    ]
