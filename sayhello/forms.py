# -*- coding: utf-8 -*-
"""
    @author: bruski wang
    @contact: bruski@qq.com
    @time: 2020/1/5
    @file: forms.py
    @desc:
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = StringField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
