# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inapp', '0011_linkedinsearchresult_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkedinsearch',
            name='geo',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Search supervisors by geo'),
        ),
        migrations.AlterField(
            model_name='linkedinsearch',
            name='companyId',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Linkedin company ID'),
        ),
        migrations.AlterField(
            model_name='linkedinsearch',
            name='search_company',
            field=models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Search term'),
        ),
    ]
