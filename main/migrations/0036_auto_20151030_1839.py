# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_film_characters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='characters',
            new_name='characters_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='director',
            new_name='director_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='episode_id',
            new_name='episode_id_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='opening_crawl',
            new_name='opening_crawl_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='producer',
            new_name='producer_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='release_date',
            new_name='release_date_url',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='title',
            new_name='title_url',
        ),
        migrations.AddField(
            model_name='film',
            name='planets_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='starships_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='vehicles_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
