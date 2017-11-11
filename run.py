# -*- coding: utf-8 -*-
from flask import (
    Flask,
    json,
    render_template,
    request,
)
from templates.Factory.ServiceFactory import userService
from templates.Model.User import User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'import_thing'


@app.route('/')
def show_posts():
    return render_template('/View/signIn.html')


@app.route('/saveUserInfo', methods=['POST', 'GET'])
def save_user_info():
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = User(EMAIL=request.form["email"],
                PASSWORD=request.form["password"])
    response = {"ResultMessage": userService.login(user=user)}
    return json.dumps(response)

@app.route('/register', methods=['POST', 'GET'])
def register():
    user = User(
                EMAIL=request.form["email"],
                PASSWORD=request.form["password"],
                NAME=request.form["name"])
    response={"ResultMessage":userService.register(user=user)}
    return json.dumps(response)

@app.route('/register.html')
def toRegister():
    return render_template("/View/register.html")

@app.route('/signIn.html')
def toSignIn():
    return render_template("/view/signIn.html")

if __name__ == '__main__':
    app.run()
