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
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 注册扩展插件
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# toolbar = DebugToolbarExtension(app)

# 避免循环依赖
from sayhello import views, commands
