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

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# --
# get env
# --
load_dotenv()
logger = create_log()


with open('config.yaml', 'r') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@{}:{}/postgres".format(doc['app']['mud']['host'], doc['app']['mud']['port']))
ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

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
    connex_app = Flask(__name__, template_folder="./templates")
    connex_app = connexion.App(__name__, specification_dir='./openapi/')
    
    @connex_app.route('/')
    def home():
        """
        This route function responds to all incoming requests
        on <URL>/
        
        :return:	A "Hello world!" string
        """
        return render_template('index.html')
            
    connex_app.add_api("swagger.yml", arguments={"title": "files"})
    CORS(connex_app.app)
    
    logger.info("Read yaml - {}".format(json.dumps(doc, indent=2)))
    logger.info('Fisihsed to read yaml ..')
    
    connex_app.app.config.update(doc)
    
    # --
    ma.init_app(connex_app.app)
    
    connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connex_app.app.config['PROPAGATE_EXCEPTIONS'] = True
    
    # @connex_app.app.before_first_request
    # def create_tables():
    #     print('--create tables..')
    #     db.create_all()
    
    db.init_app(connex_app.app)
    db.app = connex_app.app
    with connex_app.app.app_context():
        print('--create tables..')
        db.create_all()
    
    # --
    
    migrate.init_app(connex_app.app, db)
    
    return connex_app


"""
# Create the application instance
# app = Flask(__name__, template_folder="templates")
app = init_api()


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

"""

# If we're running in stand alone mode, run the application
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)
    
