from flask import Blueprint

auth = Blueprint('auth', __name__)

# 定义一个路由
@auth.route('/login')
def login():
    return "This is the login page"

@auth.route('/logout')
def logout():
    return "This is the logout page"