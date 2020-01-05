# -*- coding: utf-8 -*-
"""
    @author: bruski wang
    @contact: bruski@qq.com
    @time: 2020/1/5
    @file: views.py
    @desc:
"""
from flask import render_template, flash, redirect, url_for

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        # 处理 POST 请求
        name = form.name.data
        body = form.body.data

        # 新增一条消息到数据库
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()

        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    # 处理 GET 请求
    # 加载所有记录, 按照最新时间排序
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
