# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuruapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]