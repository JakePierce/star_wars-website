# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20151102_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='residents',
        ),
        migrations.AddField(
            model_name='planet',
            name='residents',
            field=models.ManyToManyField(to='main.People', blank=True),
        ),
    ]
