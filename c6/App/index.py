from flask import Blueprint
from Base.api_route import route
from Base.APIException import APIException

bp = Blueprint('index',__name__)

import decimal
import datetime

# @bp.route('/')
@route(bp,'/')
def index():
    result = {
        'msg':'blueprint !!!',
        'decimal':decimal.Decimal('2.3838'),
        'time':datetime.datetime.now()
    }

    a=0
    b=10

    a=b/0

    # raise APIException('error')

    # res = APIResponse(result)
    return result