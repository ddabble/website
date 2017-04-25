# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-25 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_eventregistration_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='internal',
            field=models.BooleanField(default=False, verbose_name='Intern'),
        ),
        migrations.AddField(
            model_name='event',
            name='internal',
            field=models.BooleanField(default=False, verbose_name='Intern'),
        ),
    ]
