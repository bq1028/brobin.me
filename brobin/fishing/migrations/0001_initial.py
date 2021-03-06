# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-19 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigFish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.IntegerField(choices=[(1, 'Bass'), (2, 'Crappie'), (3, 'Northern'), (4, 'Walleye')], default=3)),
                ('length', models.FloatField()),
                ('weight', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Big fish',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Saturday'), (2, 'Sunday'), (3, 'Monday'), (4, 'Tuesday'), (5, 'Wednesday'), (6, 'Thursday'), (7, 'Friday')])),
                ('bass', models.IntegerField(default=0)),
                ('crappie', models.IntegerField(default=0)),
                ('northern', models.IntegerField(default=0)),
                ('walleye', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='fishing.Year'),
        ),
        migrations.AddField(
            model_name='bigfish',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_fish', to='fishing.Year'),
        ),
    ]
