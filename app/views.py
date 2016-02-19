# coding=utf-8
from __future__ import (unicode_literals, absolute_import)
from app import app
from flask import render_template
from app.models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos)
