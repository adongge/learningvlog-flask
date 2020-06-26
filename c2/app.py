import logging

from flask import Flask

import environment

app = Flask(__name__)

app.config.from_object('Config.%s.Config'%environment.ENV)

handler = logging.FileHandler('%s/flask.log'%app.config['LOG_PATH'])
logging.root.setLevel(app.config['LOG_LEVEL'])

app.logger.addHandler(handler)

@app.route('/')
def index():
    app.logger.info('logger start')
    app.logger.error('flask error')
    return 'leaning-vlog'