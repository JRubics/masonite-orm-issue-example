import os
from masoniteorm.connections import ConnectionResolver

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'port': '3306',
        'database': 'mysql',
        'user': 'root',
        'password': 'root',
        'prefix': '',
    }
}

DB = ConnectionResolver().set_connection_details(DATABASES)
