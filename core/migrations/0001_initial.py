# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 12:15
from __future__ import unicode_literals

import core.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='Номер группы')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('geo_position', models.CharField(blank=True, max_length=60, null=True, verbose_name='Геопозиция')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('rank', core.fields.RankField(blank=True, choices=[('1', 'к.т.н'), ('2', 'д.т.н.')], max_length=1, null=True, verbose_name='Ученая степень')),
                ('position', core.fields.PositionField(choices=[('1', 'профессор'), ('2', 'доцент'), ('3', 'старший преподаватель'), ('4', 'ассистент')], max_length=1, verbose_name='Должность')),
            ],
        ),
    ]
