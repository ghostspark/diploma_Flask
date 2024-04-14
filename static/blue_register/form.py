from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField

from wtforms import validators
from wtforms.validators import DataRequired, EqualTo, Email, Length, Regexp


class ContactForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired(message="请输入用户名"), Length(0, 10)])
    Password = PasswordField("密码", validators=[DataRequired("请输入密码"), Length(6, 10)])
    Confirm = PasswordField('确认密码：', validators=[EqualTo('Password', message="两次密码不一致")])
    E_mail = StringField("电子邮箱", validators=[DataRequired(), Email(message="电子邮箱不正确")])
    submit = SubmitField("Send")
