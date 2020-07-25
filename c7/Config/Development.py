import logging

class Config:
    LOG_PATH = '/Users/adong/learning/learningvlog-flask/log'
    LOG_LEVEL = logging.NOTSET

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@docker.for.mac.host.internal/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True