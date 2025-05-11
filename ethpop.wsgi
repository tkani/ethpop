#!/usr/bin/python3.8

# Activate the virtual environment
# activate_this = '/var/www/jabali/venv/bin/activate_this.py'
# exec(open(activate_this).read(), dict(__file__=activate_this))

# Add the application path to sys.path
import sys
# print("Python version")

# print(sys.version)

sys.path.insert(0, "/var/www/ethpop")

# Import the Flask app instance
from ethpop import app as application