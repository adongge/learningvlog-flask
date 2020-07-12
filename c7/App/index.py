from flask import Blueprint
from Base.api_route import route
from Base.APIException import APIException

bp = Blueprint('index',__name__)

import decimal
import datetime

from Models.User import User

# @bp.route('/')
@route(bp,'/')
def index():
    users = User.query.all()
    return users