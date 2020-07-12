import logging
import environment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('Config.%s.Config'%environment.ENV)
db = SQLAlchemy(app)

from Base import error_handlers
from Base.JSONEncoder import JSONEncoder
app.json_encoder = JSONEncoder

handler = logging.FileHandler('%s/flask.log'%app.config['LOG_PATH'])
logging.root.setLevel(app.config['LOG_LEVEL'])
app.logger.addHandler(handler)