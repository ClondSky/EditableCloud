# -*- coding: utf-8 -*-
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from templates.UserData.UserDao import UserDao
from templates.PO.User import User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'import_thing'


@app.route('/')
def show_posts():
    return render_template('/index.html')


@app.route('/submitUser')
def submitUser():

    return UserDao.insertUser()


if __name__ == '__main__':
    app.run()
