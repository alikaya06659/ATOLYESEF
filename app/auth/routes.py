from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm, UpdateProfileForm
from app.models import User, Reservation
import os
from werkzeug.utils import secure_filename
from flask import current_app

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Giriş başarılı, hoş geldiniz!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Hatalı kullanıcı adı veya şifre!', 'danger')
    return render_template('auth/login.html', title='Giriş Yap', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt başarılı, giriş yapabilirsiniz.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Kayıt Ol', form=form)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Kullanıcı profil sayfası – sadece oturum açık kullanıcılar erişebilir."""
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.avatar.data:
            f = form.avatar.data
            filename = secure_filename(f.filename)
            unique_filename = f"{current_user.id}_{filename}"
            avatars_dir = os.path.join(current_app.root_path, 'static', 'avatars')
            os.makedirs(avatars_dir, exist_ok=True)
            f.save(os.path.join(avatars_dir, unique_filename))
            current_user.avatar = unique_filename
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profiliniz başarıyla güncellendi.', 'success')
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    # Rezervasyonları çek (SQLAlchemy 2.x stili)
    stmt = db.select(Reservation).where(Reservation.user_id == current_user.id).order_by(Reservation.borrow_date.desc())
    reservations = db.session.scalars(stmt).all()
    
    return render_template('auth/profile.html', title='Profil', form=form, reservations=reservations)
