#!/bin/bash

python manage.py migrate
python manage.py loaddata movie.json
python manage.py runserver 0.0.0.0:8000