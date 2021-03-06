# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0004_auto_20170810_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='access_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_id', models.CharField(max_length=43)),
                ('roll_number', models.IntegerField()),
                ('is_filled', models.BooleanField(default=False)),
                ('filled_option', models.CharField(max_length=25)),
                ('is_blocked', models.BooleanField(default=False)),
            ],
        ),
    ]
