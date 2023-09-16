#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations web
python manage.py migrate
python manage.py load_shop_data
