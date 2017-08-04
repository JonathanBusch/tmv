# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0125_doc_relevant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docauthinst',
            name='AF',
            field=models.TextField(db_index=True, null=True, verbose_name='Author Full Name'),
        ),
        migrations.AlterField(
            model_name='docauthinst',
            name='AU',
            field=models.TextField(db_index=True, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='docauthinst',
            name='institution',
            field=models.TextField(db_index=True, verbose_name='Institution Name'),
        ),
    ]
