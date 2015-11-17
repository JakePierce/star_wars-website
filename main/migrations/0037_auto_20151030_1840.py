# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20151030_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='director_url',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='episode_id_url',
            new_name='episode_id',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='opening_crawl_url',
            new_name='opening_crawl',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='producer_url',
            new_name='producer',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='release_date_url',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='title_url',
            new_name='title',
        ),
    ]
