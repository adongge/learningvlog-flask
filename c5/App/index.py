from flask import Blueprint
from Base.api_route import route

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

    # res = APIResponse(result)
    return result