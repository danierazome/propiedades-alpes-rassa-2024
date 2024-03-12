import os
import time


def database_url():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


def broker_host():
  return '172.17.0.2'
    # return os.environ['PULSAR_HOST']


def time_millis():
    return int(time.time() * 1000)
