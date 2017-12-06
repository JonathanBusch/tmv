# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 15:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0055_runstats_empty_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDocTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_docs', models.IntegerField()),
                ('dt_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeDTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('dtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmv_app.DynamicTopic')),
            ],
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, null=True)),
                ('ys', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.AddField(
            model_name='timedtopic',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmv_app.TimePeriod'),
        ),
        migrations.AddField(
            model_name='timedoctotal',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmv_app.TimePeriod'),
        ),
        migrations.AddField(
            model_name='timedoctotal',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmv_app.RunStats'),
        ),
    ]
