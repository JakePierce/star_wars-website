# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('mass', models.IntegerField(null=True, blank=True)),
                ('hair_color', models.CharField(max_length=20, null=True, blank=True)),
                ('skin_color', models.CharField(max_length=20, null=True, blank=True)),
                ('eye_color', models.CharField(max_length=20, null=True, blank=True)),
                ('birth_year', models.CharField(max_length=20, null=True, blank=True)),
                ('gender', models.CharField(max_length=20, null=True, blank=True)),
                ('homeworld', models.CharField(max_length=100, null=True, blank=True)),
                ('films', models.CharField(max_length=100, null=True, blank=True)),
                ('species', models.CharField(max_length=100, null=True, blank=True)),
                ('vehicles', models.CharField(max_length=100, null=True, blank=True)),
                ('starships', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('rotation_period', models.IntegerField(null=True, blank=True)),
                ('orbital_period', models.IntegerField(null=True, blank=True)),
                ('diameter', models.IntegerField(null=True, blank=True)),
                ('climate', models.CharField(max_length=20, null=True, blank=True)),
                ('gravity', models.CharField(max_length=20, null=True, blank=True)),
                ('terrain', models.CharField(max_length=20, null=True, blank=True)),
                ('surface_water', models.IntegerField(null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('residents', models.CharField(max_length=100, null=True, blank=True)),
                ('films', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('designation', models.CharField(max_length=20, null=True, blank=True)),
                ('average_height', models.IntegerField(null=True, blank=True)),
                ('skin_colors', models.CharField(max_length=100, null=True, blank=True)),
                ('hair_colors', models.CharField(max_length=100, null=True, blank=True)),
                ('eye_colors', models.CharField(max_length=100, null=True, blank=True)),
                ('average_lifespan', models.IntegerField(null=True, blank=True)),
                ('homeworld', models.CharField(max_length=100, null=True, blank=True)),
                ('language', models.CharField(max_length=100, null=True, blank=True)),
                ('people', models.CharField(max_length=100, null=True, blank=True)),
                ('films', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('model', models.CharField(max_length=20, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=40, null=True, blank=True)),
                ('cost_in_credits', models.IntegerField(max_length=40, null=True, blank=True)),
                ('length', models.IntegerField(null=True, blank=True)),
                ('max_atmosphering_speed', models.IntegerField(null=True, blank=True)),
                ('crew', models.IntegerField(null=True, blank=True)),
                ('passengers', models.IntegerField(null=True, blank=True)),
                ('cargo_capacity', models.IntegerField(null=True, blank=True)),
                ('consumables', models.CharField(max_length=40, null=True, blank=True)),
                ('hyperdrive_rating', models.FloatField(null=True, blank=True)),
                ('MGLT', models.IntegerField(null=True, blank=True)),
                ('starship_class', models.CharField(max_length=100, null=True, blank=True)),
                ('pilots', models.CharField(max_length=200, null=True, blank=True)),
                ('films', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('model', models.CharField(max_length=150, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=150, null=True, blank=True)),
                ('cost_in_credits', models.IntegerField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('max_atmosphering_speed', models.IntegerField(null=True, blank=True)),
                ('crew', models.IntegerField(null=True, blank=True)),
                ('passengers', models.IntegerField(null=True, blank=True)),
                ('cargo_capacity', models.IntegerField(null=True, blank=True)),
                ('consumables', models.IntegerField(null=True, blank=True)),
                ('vehicle_class', models.CharField(max_length=200, null=True, blank=True)),
                ('pilots', models.CharField(max_length=200, null=True, blank=True)),
                ('films', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
