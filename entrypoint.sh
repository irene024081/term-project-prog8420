#!/bin/sh
echo "Performing data migration"
poetry run python manage.py migrate --noinput

echo "Create Admin User"
poetry run python manage.py initadmin $ADMIN_NAME $ADMIN_EMAIL $ADMIN_PASSWORD

echo "Starting server"
poetry run hypercorn movie_review.asgi:application --bind 0.0.0.0:8000