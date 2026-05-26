from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    password_confirm = PasswordField('Şifre Tekrar', validators=[DataRequired(), EqualTo('password', message='Şifreler eşleşmiyor.')])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Bu kullanıcı adı zaten kullanımda.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Bu e-posta adresi zaten kayıtlı.')

class LoginForm(FlaskForm):
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')
