# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENo', models.IntegerField()),
                ('EName', models.CharField(max_length=64)),
                ('ESal', models.IntegerField()),
                ('ELoct', models.CharField(max_length=64)),
            ],
        ),
    ]
