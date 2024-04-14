from flask import request, flash, render_template

import sql
from static.blue_register import register_blue
from static.blue_register.form import ContactForm


@register_blue.route('/register', methods=['POST', 'GET'])
def register():
    form = ContactForm()

    if request.method == 'POST':
        data = [{'name': form.name.data, 'pw': form.Password.data, 'e_mail': form.E_mail.data}]
        print(data)
        if form.validate():
            flash('All fields are required.')
            # sql.mysql_insert(data)
            return render_template('./html/login.html', form=form)
        else:
            print(form.errors)
            return render_template('./html/register.html', form=form)
    elif request.method == 'GET':
        return render_template('./html/register.html', form=form)
