import os
import time


def database_url():
    return 'postgresql://user:password@172.23.0.2:5432/alpes'
    # return os.environ['DB_URL']


def broker_host():
    return '172.17.0.2'


def time_millis():
    return int(time.time() * 1000)
