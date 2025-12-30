# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import os
from pathlib import Path

# --- Load environment variables from ~/.bashrc ---
bashrc = Path.home() / ".bashrc"
if bashrc.exists():
    for line in bashrc.read_text().splitlines():
        if line.startswith("export "):
            key, value = line.replace("export ", "").split("=", 1)
            os.environ[key] = value.strip('"')

# add your project directory to the sys.path
project_home = '/home/democracy1434/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from server import app as application  # noqa
