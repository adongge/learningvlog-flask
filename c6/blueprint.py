from app import app

from App import index

app.register_blueprint(index.bp,url_prefix='/')

# print(app.url_map)