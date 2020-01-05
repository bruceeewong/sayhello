# -*- coding: utf-8 -*-
"""
    @author: bruski wang
    @contact: bruski@qq.com
    @time: 2020/1/5
    @file: __init__.py.py
    @desc: sayhello 构造文件
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# 避免循环依赖
from sayhello import views, commands
