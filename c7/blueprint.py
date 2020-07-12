from app import app
from flask import send_from_directory
from App import index

@index.bp.route('/favicon.ico')
def favicon():
    return send_from_directory('/Users/adong/learning/learningvlog-flask','favicon.ico', mimetype='image/vnd.microsoft.icon')

app.register_blueprint(index.bp,url_prefix='/')