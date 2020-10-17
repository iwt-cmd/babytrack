#!/bin/bash

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' > key
cat key
export SECRET_KEY=$(cat key)
echo $SECRET_KEY
gunicorn --bind 0.0.0.0:8000 --workers 3 baby_tracking.wsgi