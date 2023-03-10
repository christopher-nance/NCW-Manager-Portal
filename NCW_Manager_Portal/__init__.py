"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import NCW_Manager_Portal.views
