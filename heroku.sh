#!/usr/bin/env bash
python remove_migrations.py
python manage.py makemigrations api
python manage.py makemigrations core
python manage.py migrate