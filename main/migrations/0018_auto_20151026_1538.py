# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151026_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='films',
            field=models.ManyToManyField(to='main.Film', blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='films',
            field=models.ManyToManyField(to='main.Film', blank=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='films',
            field=models.ManyToManyField(to='main.Film', blank=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='films',
            field=models.ManyToManyField(to='main.Film', blank=True),
        ),
    ]
