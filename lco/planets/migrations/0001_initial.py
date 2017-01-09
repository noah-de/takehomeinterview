# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('size', models.FloatField()),
                ('distance', models.FloatField()),
                ('ordinality', models.IntegerField(unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]