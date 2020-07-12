# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from Base import db
from Models.BaseModel import BaseModel



class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    username = db.Column(db.String(16), nullable=False, unique=True, info='用户名')
    nickname = db.Column(db.String(32), nullable=False, info='昵称')
    description = db.Column(db.String(200), info='描述')
    password = db.Column(db.String(64), nullable=False, info='密码')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户状态，0 正常，1禁用')
    mobile = db.Column(db.String(15), nullable=False, server_default=db.FetchedValue(), info='手机号')
    update_dt = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    create_dt = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
