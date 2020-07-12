from Base import db

class BaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def to_dict(obj):
        res={}
        for c in obj.__table__.columns:
            value=getattr(obj,c.name,'')
            res[c.name]=value
        return res