from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm, UpdateProfileForm
from app.models import User, Reservation, Notification
import os
from werkzeug.utils import secure_filename
from flask import current_app

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
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
    if current_user.username == 'admin':
        stmt = db.select(Reservation).order_by(Reservation.borrow_date.desc())
    else:
        stmt = db.select(Reservation).where(Reservation.user_id == current_user.id).order_by(Reservation.borrow_date.desc())
    reservations = db.session.scalars(stmt).all()
    
    return render_template('auth/profile.html', title='Profil', form=form, reservations=reservations)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız.', 'info')
    return redirect(url_for('main.index'))

@bp.route('/send_message/<int:recipient_id>', methods=['POST'])
@login_required
def send_message(recipient_id):
    # Eğer gönderen admin değilse, sadece admin'e mesaj atabilir.
    if current_user.username != 'admin':
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user or recipient_id != admin_user.id:
            abort(403)
    
    content = request.form.get('message_content')
    if not content or not content.strip():
        flash('Mesaj içeriği boş olamaz.', 'danger')
        return redirect(request.referrer or url_for('auth.profile'))
        
    notification = Notification(
        sender_id=current_user.id,
        recipient_id=recipient_id,
        content=content.strip()
    )
    db.session.add(notification)
    db.session.commit()
    
    flash('Mesajınız başarıyla iletildi.', 'success')
    return redirect(request.referrer or url_for('auth.profile'))

@bp.route('/notifications')
@login_required
def notifications():
    stmt = db.select(Notification).where(Notification.recipient_id == current_user.id).order_by(Notification.created_at.desc())
    user_notifications = db.session.scalars(stmt).all()
    
    stmt_sent = db.select(Notification).where(Notification.sender_id == current_user.id).order_by(Notification.created_at.desc())
    sent_notifications = db.session.scalars(stmt_sent).all()
    
    admin_user = None
    if current_user.username != 'admin':
        admin_user = User.query.filter_by(username='admin').first()
        
    return render_template('auth/notifications.html', title='Bildirimler', notifications=user_notifications, sent_notifications=sent_notifications, admin_user=admin_user)

@bp.route('/read_notification/<int:id>', methods=['POST'])
@login_required
def read_notification(id):
    notification = db.get_or_404(Notification, id)
    if notification.recipient_id != current_user.id:
        abort(403)
        
    notification.is_read = True
    db.session.commit()
    return redirect(url_for('auth.notifications'))
