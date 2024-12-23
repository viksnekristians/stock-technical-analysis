# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    default-libmysqlclient-dev \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

COPY crontab /etc/cron.d/dev_server_crons

# Apply the cron job
RUN chmod 0644 /etc/cron.d/dev_server_crons
RUN crontab /etc/cron.d/dev_server_crons
