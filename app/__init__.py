# coding=utf-8
from __future__ import (unicode_literals, absolute_import)
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

from app import views, models
