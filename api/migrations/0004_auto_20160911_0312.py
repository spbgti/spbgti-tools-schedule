# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160911_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название занятия'),
        ),
    ]
