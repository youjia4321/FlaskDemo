import re

from flask import Blueprint, request, session, redirect, url_for, render_template, jsonify
from dao import user_dao, article_dao, comment_dao
from mainapp.views import article

blue = Blueprint('userBlue', __name__)

dao = user_dao.UserDao()
a_dao = article_dao.ArticleDao()
comment_dao = comment_dao.CommentDao()


@blue.route('/index', methods=['GET'])
def index():
    num = 3
    articles, index, pages = article.article_page(1, num)
    if not session.get('login_user'):  # 验证用户是否登录
        if articles:
            return render_template('index.html', articles=articles[0])
        return render_template('index.html', articles=[])
    user = session.get('login_user')[0]
    return render_template('index.html', user=user, articles=articles, index=index, pages=pages, num=num, page=1)


@blue.route('/login', methods=['POST'])
def login():
    if request.method == "POST":

        username = request.form.get('username', None)
        password = request.form.get('password', None)
        print(username, password)
        if all((username, password)):
            user, result = dao.login(username, password)
            if user:
                session['login_user'] = user
                msg = '用户登录成功'
                code = 200
            else:
                msg = '账户或者密码有误'
                code = 404
        else:
            msg = '账户或者密码不能为空'
            code = 10001

        context = locals()
        return jsonify(**context)


@blue.route('/register', methods=['POST'])
def register():
    if request.method == "POST":

        username = request.form.get('username', None)
        password = request.form.get('password', None)
        cpassword = request.form.get('cpassword', None)
        email = request.form.get('email', None)
        phone = request.form.get('phone', None)
        print(username, password, cpassword, email, phone)

        if all((username, password, cpassword, email, phone)):
            if re.match(r"^[\u4e00-\u9fa5_a-zA-Z0-9]+$", username):
                if len(password) >= 6:
                    if re.match(r"^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$", password):
                        if password == cpassword:
                            if re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
                                data = {
                                    "username": username,
                                    "password": password,
                                    'email': email,
                                    'phone': phone
                                }
                                result = dao.register(**data)
                                if result['status'] == 200:
                                    msg = '用户注册成功'
                                    code = 200
                                else:
                                    msg = '用户已存在，请重新输入'
                                    code = 404
                            else:
                                msg = '邮箱格式不正确'
                                code = 403
                        else:
                            msg = '两次密码不一致'
                            code = 10004
                    else:
                        msg = '密码包含字母、数字、符号两者'
                        code = 10005
                else:
                    msg = '密码长度不能小于6位'
                    code = 10003
            else:
                msg = '用户名包含非法字符'
                code = 10002
        else:
            msg = '账户、密码或邮箱不能为空'
            code = 10001

        context = locals()
        return jsonify({'code': code, 'msg': msg})


@blue.route('/logout', methods=['GET'])
def logout():
    del session['login_user']
    return redirect(url_for('index'))

