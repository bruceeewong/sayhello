# -*- coding: utf-8 -*-
"""
    @author: bruski wang
    @contact: bruski@qq.com
    @time: 2020/1/5
    @file: commands.py
    @desc:
"""
import click

from sayhello import app, db


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized databases')
