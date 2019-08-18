# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-14 06:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityTemperature',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('temperature', models.CharField(max_length=500)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('location_city', models.CharField(max_length=50)),
                ('location_state', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'city_temperature',
            },
        ),
    ]