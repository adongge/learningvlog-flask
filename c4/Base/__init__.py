import logging

from flask import Flask

import environment

app = Flask(__name__)

app.config.from_object('Config.%s.Config'%environment.ENV)

handler = logging.FileHandler('%s/flask.log'%app.config['LOG_PATH'])
logging.root.setLevel(app.config['LOG_LEVEL'])

app.logger.addHandler(handler)