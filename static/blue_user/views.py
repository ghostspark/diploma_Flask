import re

from flask import request, render_template, session, redirect

import sql
from static.blue_user import user_blue
from static.blue_user.forms import u_PasswordForm


@user_blue.route('/user', methods=['GET', 'POST'])
def user():
    print(session['name'])
    if request.method == 'POST':
        # li = sql.mysql_user_select_alldata(data[0]['name'])
        return render_template('./html/index.html')
    elif request.method == 'GET':
        li = sql.mysql_user_select_alldata(session['name'])
        return render_template('./html/test_user.html', li=li)


@user_blue.route('/user/update/username=<name>', methods=['GET', 'POST'])
def update_pw(name):
    if request.method == 'GET':
        form = u_PasswordForm()
        session['up_u_name'] = request.full_path
        return render_template("./html/update/password_user.html", forms=form)
    elif request.method == 'POST':
        form = u_PasswordForm()
        print(form.errors)
        if form.validate():
            N_password = form.Password.data
            name = re.split('\?', re.split('=', session['up_u_name'])[1])[0]
            print(name)
            try:
                sql.mysql_userpw_alter(name, N_password)
            except Exception as e:
                print(e)
            return redirect('/user')
        else:
            return render_template("./html/update/password_user.html", forms=form)
