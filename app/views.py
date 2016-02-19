# coding=utf-8
from __future__ import (unicode_literals, absolute_import)
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', text='hello world')
