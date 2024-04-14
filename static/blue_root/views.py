import re

from flask import request, render_template, g, redirect, session

import sql
from sql_exts import db
from static.blue_root import root_blue, forms
from static.blue_root.forms import PasswordForm, EmailForm


class User(db.Model):
    __tablename__ = 'user_test'
    user_name = db.Column(db.String(50), primary_key=True)
    user_pw = db.Column(db.String(50))
    user_email = db.Column(db.String(50))

    def __init__(self, user_name, user_pw, user_email):
        self.user_name = user_name
        self.user_pw = user_pw
        self.user_email = user_email

    def __repr__(self):  # 自定义 交互模式 & print() 的对象打印
        return "(%s,%s,%s)" % (self.user_name, self.user_pw, self.user_email)


# @root_blue.before_request
# def before():
#     url = request.path
#     print(url)


@root_blue.route("/root", methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        userlist = sql.mysql_root_select_alluser()
        return render_template("./html/test_root.html", userlist=userlist)
    elif request.method == 'POST':
        return render_template("html/test_root.html")


@root_blue.route("/delete/username=<name>", methods=['GET', 'POST'])
def data_del(name):
    g.name = name
    print(g.name)
    if request.method == 'GET':
        sql.mysql_user_delete(name)
        return redirect('/root')
    elif request.method == 'POST':
        userlist = []
        return render_template("html/test_root.html", userlist=userlist)


@root_blue.route("/update-pw/username=<name>", methods=['GET', 'POST'])
def data_up_pw(name):

    if request.method == 'GET':
        forms_r = PasswordForm()
        session['up_name'] = request.full_path
        return render_template("html/update/password.html", forms=forms_r)

    elif request.method == 'POST':
        forms = PasswordForm()
        print(forms.errors)
        if forms.validate():
            N_password = forms.Password.data
            name = re.split('\?', re.split('=', session['up_name'])[1])[0]
            print(name)
            try:
                sql.mysql_userpw_alter(name, N_password)
            except Exception as e:
                print(e)
            return redirect('/root')
        else:
            return render_template("./html/update/password.html", forms=forms)


@root_blue.route("/update-ma/username=<name>", methods=['GET', 'POST'])
def data_up_em(name):

    if request.method == 'GET':
        forms_r = EmailForm()
        session['up_email'] = request.full_path
        return render_template("html/update/email.html", forms=forms_r)

    elif request.method == 'POST':
        forms = EmailForm()
        print(forms.errors)
        if forms.validate():
            N_email = forms.Email.data
            name = re.split('\?', re.split('=', session['up_email'])[1])[0]
            print(name)
            try:
                sql.mysql_email_alter(name, N_email)
            except Exception as e:
                print(e)
            return redirect('/root')
        else:
            return render_template("./html/update/email.html", forms=forms)