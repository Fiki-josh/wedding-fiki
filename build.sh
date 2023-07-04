#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies using pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate
