# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151023_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='films',
        ),
        migrations.AddField(
            model_name='people',
            name='films',
            field=models.ManyToManyField(to='main.Film', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='planet',
            name='films',
        ),
        migrations.AddField(
            model_name='planet',
            name='films',
            field=models.ManyToManyField(to='main.Film', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='species',
            name='films',
        ),
        migrations.AddField(
            model_name='species',
            name='films',
            field=models.ManyToManyField(to='main.Film', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='starship',
            name='films',
        ),
        migrations.AddField(
            model_name='starship',
            name='films',
            field=models.ManyToManyField(to='main.Film', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='films',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='films',
            field=models.ManyToManyField(to='main.Film', null=True, blank=True),
        ),
    ]
