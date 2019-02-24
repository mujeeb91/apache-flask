import sys

project_path = "/var/www/flask_app"
sys.path.insert(0, project_path)

from server import app as application
