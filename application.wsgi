import sys
sys.path.insert(0, '/var/www/html/v1')

import os
from dotenv import load_dotenv
load_dotenv('/var/www/html/v1/.env')

from flask_app.app import app as application