from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import User
from app import db
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

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

class UpdateProfileForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    avatar = FileField('Profil Fotoğrafı', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Sadece resim dosyaları (.jpg, .jpeg, .png) yüklenebilir.')
    ])
    submit = SubmitField('Güncelle')

    def validate_username(self, field):
        if field.data != current_user.username:
            if db.session.execute(db.select(User).filter_by(username=field.data)).scalar_one_or_none():
                raise ValidationError('Bu kullanıcı adı zaten kullanımda.')

    def validate_email(self, field):
        if field.data != current_user.email:
            if db.session.execute(db.select(User).filter_by(email=field.data)).scalar_one_or_none():
                raise ValidationError('Bu e-posta adresi zaten kayıtlı.')
