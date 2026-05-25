from flask import render_template, redirect, url_for, flash
from app.auth import bp
from app.auth.forms import LoginForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Giriş isteği alındı!')
        return redirect(url_for('main.index'))
    return render_template('base.html', title='Giriş Yap', form=form)

@bp.route('/logout')
def logout():
    flash('Başarıyla çıkış yapıldı!')
    return redirect(url_for('main.index'))
