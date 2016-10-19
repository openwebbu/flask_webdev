from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy # database interfacing

app_obj = Flask(__name__) # Initialize Flask web application object
# app_obj.config.from_object('config') # use database path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app_obj) # create database

from app import views # This is the app folder in which views are located
# from app import models
