#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure the cron jobs file has the correct permissions
chmod 0644 /etc/cron.d/dev_server_crons

# Load the cron jobs
crontab /etc/cron.d/dev_server_crons

# Wait for MySQL to be ready
./wait-for-it.sh mysql-db:3306 -- 

# Start cron
cron

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000
