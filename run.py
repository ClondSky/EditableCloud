# -*- coding: utf-8 -*-
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    json,
    render_template,
    request,
    url_for,
)
from templates.Factory.DataFactory import userDao
from templates.Model.User import User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'import_thing'


@app.route('/')
def show_posts():
    return render_template('/View/signIn.html')


@app.route('/saveUserInfo', methods=['POST', 'GET'])
def saveUserInfo():
    data = json.loads(request.form.data, encoding="utf-8")
    user = User();
    user.userName = "123"
    user.passWord = "123"
    user.email = data["email"]
    return userDao.saveUserInfo(user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = {"ResultMessage": "success"}
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
