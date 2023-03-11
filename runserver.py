
"""
This script runs the NCW_Manager_Portal application using a development server.

For deployment on Azure, app.py will be used.
"""

from os import environ
from NCW_Manager_Portal import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
