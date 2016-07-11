# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=3000)),
                ('excerpt', models.CharField(max_length=3000)),
                ('client', models.CharField(max_length=3000)),
                ('location', models.CharField(max_length=3000)),
                ('url', models.CharField(max_length=3000)),
            ],
        ),
    ]
