import logging

from flask import Flask
app = Flask(__name__)

from Base import error_handlers
from Base.JSONEncoder import JSONEncoder

import environment



app.json_encoder = JSONEncoder

app.config.from_object('Config.%s.Config'%environment.ENV)

handler = logging.FileHandler('%s/flask.log'%app.config['LOG_PATH'])
logging.root.setLevel(app.config['LOG_LEVEL'])

app.logger.addHandler(handler)