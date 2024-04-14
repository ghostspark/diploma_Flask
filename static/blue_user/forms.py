from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField

from wtforms import validators
from wtforms.validators import DataRequired, EqualTo, Email, Length, Regexp


class u_PasswordForm(FlaskForm):
    Password = PasswordField("修改密码", validators=[DataRequired("请输入密码"), Length(6, 10)])
    Confirm = PasswordField('确认密码：', validators=[EqualTo('Password', message="两次密码不一致")])
    submit = SubmitField("Send")


# class u_ScaleForm(FlaskForm):


