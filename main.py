import connexion
from flask import (
    Flask,
    render_template
)
from flask_cors import CORS
from config.log_config import create_log
import yaml
from dotenv import load_dotenv
import os
import json

# --
# get env
# --
load_dotenv()
logger = create_log()

"""
# Create the application instance
app = Flask(__name__, template_folder="templates")
# Create the application instance
app = connexion.App(__name__, specification_dir='./openapi/')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')
"""

# Connexion is a Python web framework that makes spec-first and api-first development easy
# With Connexion, you write your API specification first, and automatically get a lot of functionality.
# server_args={'static_folder'='../frontEnd/static', 'template_folder'='../frontEnd/templates'})
def init_api():
    # Create the application instance
    connex_app = Flask(__name__, template_folder="templates")
    connex_app = connexion.App(__name__, specification_dir='./openapi/')
    connex_app.add_api("swagger.yml", arguments={"title": "files"})
    CORS(connex_app.app)
    
    return connex_app


# Create the application instance
# app = Flask(__name__, template_folder="templates")
app = init_api()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('index.html')



# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
