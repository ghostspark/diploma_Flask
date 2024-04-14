from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

import sql


class loginForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired("输入用户名.")])
    Password = PasswordField("密码", validators=[DataRequired("请输入密码")])
    Remember = BooleanField("remember me")
    submit = SubmitField("Send")
