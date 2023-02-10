from flask import Blueprint,render_template

user = Blueprint('user', __name__)

@user.route('/user/login')
def login():
    return '登录成功'

@user.route('/user/info')
def info():
    return render_template('user_info.html',
                           name='xiao',
                           sex='male',
                           age=26,
                           phone=['138383838', '01234568910'])
