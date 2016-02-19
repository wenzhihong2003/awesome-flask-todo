# coding=utf-8
from __future__ import (unicode_literals, absolute_import)

from app import db
import datetime

class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)
