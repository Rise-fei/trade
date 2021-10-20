# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2021-06-07 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('customer', models.CharField(max_length=128)),
            ],
        ),
    ]