from flask.json import JSONEncoder as BaseJSONEncoder

import datetime
import decimal

from Models.BaseModel import BaseModel

class JSONEncoder(BaseJSONEncoder):
    def default(self,o):
        if isinstance(o,datetime.datetime):
            return o.strftime('%Y-%m-%d %H-%M-%S')
        if isinstance(o,decimal.Decimal):
            return float(o)
        # 其他
        if isinstance(o,BaseModel):
            return o.to_dict(o)

        return super(JSONEncoder,self).default(o)