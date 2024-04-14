from flask import request, render_template, flash, redirect, url_for, session

import sql
from static.blue_log import log_blue
from static.blue_log.form import loginForm


@log_blue.route('/login', methods=['GET', 'POST'])  # login
def login():
    form = loginForm()
    if request.method == 'POST':
        session['name'] = form.name.data
        session['password'] = form.Password.data
        data = [{'name': form.name.data, 'pw': form.Password.data, 'remember': form.Remember.data}]
        if data[0]['name'] == sql.mysql_select_user(data[0]['name'])[0] and data[0]['pw'] == \
                sql.mysql_select_user(name=data[0]['name'])[1]:
            if sql.mysql_select_user(data[0]['name'])[3] == '0':
                return redirect('/root')
            else:
                li = sql.mysql_user_select_alldata(data[0]['name'])
                return render_template('./html/test_user.html', li=li)
                # return redirect('/user')
        else:
            print(data)
            return render_template('./html/login.html', form=form)
    elif request.method == 'GET':
        return render_template('./html/login.html', form=form)
