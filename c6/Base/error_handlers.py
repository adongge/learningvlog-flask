from Base import app
from Base.APIException import APIException
import traceback

@app.errorhandler(Exception)
def framework_error(e):
    msg=str(e)
    code=500
    if isinstance(e,APIException):
        msg=e.msg
        code=e.code

    app.logger.error(traceback.format_exc())
    return APIException(msg=msg,code=code)