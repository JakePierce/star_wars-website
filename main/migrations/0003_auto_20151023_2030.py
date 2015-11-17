# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151023_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('episode_id', models.IntegerField(null=True, blank=True)),
                ('opening_crawl', models.CharField(max_length=500, null=True, blank=True)),
                ('director', models.CharField(max_length=20, null=True, blank=True)),
                ('producer', models.CharField(max_length=20, null=True, blank=True)),
                ('release_date', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='people',
            name='films',
            field=models.ForeignKey(blank=True, to='main.Film', null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='films',
            field=models.ForeignKey(blank=True, to='main.Film', null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='films',
            field=models.ForeignKey(blank=True, to='main.Film', null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='films',
            field=models.ForeignKey(blank=True, to='main.Film', null=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='films',
            field=models.ForeignKey(blank=True, to='main.Film', null=True),
        ),
    ]
