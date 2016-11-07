from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy # database interfacing

app_obj = Flask(__name__)
app_obj.config.from_object('config') # use database path
app_obj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app_obj) # create database

from app import views
from app import models
