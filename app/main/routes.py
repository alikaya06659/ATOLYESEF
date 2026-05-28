from flask import render_template, redirect, url_for, flash, request, abort, jsonify
from flask_login import login_required
from app import db
from app.main import bp
from app.main.forms import EquipmentForm
from app.models import Equipment, Reservation
from flask_login import current_user
from datetime import datetime

# ---------------------------------------------------------------------------
# Ana sayfa (ileride yönlendirme amaçlı)
# ---------------------------------------------------------------------------
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('base.html', title='Anasayfa')

# ---------------------------------------------------------------------------
# Ekipman listesi - Sayfalama + Arama
# ---------------------------------------------------------------------------
@bp.route('/equipments')
def equipments():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search = request.args.get('q', '').strip()

    if search:
        pattern = f"%{search}%"
        stmt = db.select(Equipment).where(
            db.or_(
                Equipment.name.ilike(pattern),
                Equipment.code.ilike(pattern),
                Equipment.laboratory.ilike(pattern),
            )
        ).order_by(Equipment.id.desc())
    else:
        stmt = db.select(Equipment).order_by(Equipment.id.desc())

    pagination = db.paginate(stmt, page=page, per_page=per_page)
    equipments = pagination.items
    return render_template(
        'equipment_list.html',
        equipments=equipments,
        pagination=pagination,
        search=search,
    )

# ---------------------------------------------------------------------------
# Yeni ekipman ekleme
# ---------------------------------------------------------------------------
@bp.route('/equipment/new', methods=['GET', 'POST'])
@login_required
def equipment_create():
    form = EquipmentForm()
    if form.validate_on_submit():
        new_eq = Equipment(
            name=form.name.data,
            code=form.code.data,
            laboratory=form.laboratory.data,
            status=form.status.data,
        )
        db.session.add(new_eq)
        db.session.commit()
        flash('Ekipman başarıyla eklendi.', 'success')
        return redirect(url_for('main.equipments'))
    return render_template('equipment_form.html', form=form, title='Yeni Ekipman')

# ---------------------------------------------------------------------------
# Ekipman düzenleme
# ---------------------------------------------------------------------------
@bp.route('/equipment/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def equipment_edit(id):
    equipment = db.get_or_404(Equipment, id)
    form = EquipmentForm(obj=equipment)
    if form.validate_on_submit():
        equipment.name = form.name.data
        equipment.code = form.code.data
        equipment.laboratory = form.laboratory.data
        equipment.status = form.status.data
        db.session.commit()
        flash('Ekipman başarıyla güncellendi.', 'success')
        return redirect(url_for('main.equipments'))
    return render_template('equipment_form.html', form=form, title='Ekipman Düzenle')

# ---------------------------------------------------------------------------
# Ekipman silme (POST)
# ---------------------------------------------------------------------------
@bp.route('/equipment/<int:id>/delete', methods=['POST'])
@login_required
def equipment_delete(id):
    equipment = db.get_or_404(Equipment, id)
    db.session.delete(equipment)
    db.session.commit()
    flash('Ekipman başarıyla silindi.', 'success')
    return redirect(url_for('main.equipments'))

# ---------------------------------------------------------------------------
# Ekipman Ödünç Alma (POST)
# ---------------------------------------------------------------------------
@bp.route('/equipment/<int:id>/borrow', methods=['POST'])
@login_required
def equipment_borrow(id):
    equipment = db.get_or_404(Equipment, id)
    if equipment.status != 'Mevcut':
        flash('Bu ekipman şu anda kullanılamaz.', 'danger')
        return redirect(url_for('main.equipments'))
    
    equipment.status = 'Kullanımda'
    reservation = Reservation(
        user_id=current_user.id,
        equipment_id=equipment.id,
        borrow_date=datetime.utcnow()
    )
    db.session.add(reservation)
    db.session.commit()
    flash('Ekipman başarıyla ödünç alındı.', 'success')
    return redirect(url_for('main.equipments'))

# ---------------------------------------------------------------------------
# Ekipman İade Etme (POST)
# ---------------------------------------------------------------------------
@bp.route('/reservation/<int:id>/return', methods=['POST'])
@login_required
def equipment_return(id):
    reservation = db.get_or_404(Reservation, id)
    # Yetki kontrolü: Sadece kendi aldığı ekipmanı iade edebilir
    if reservation.user_id != current_user.id:
        abort(403)
    
    if reservation.is_returned:
        flash('Bu ekipman zaten iade edilmiş.', 'info')
        return redirect(url_for('auth.profile'))
        
    reservation.is_returned = True
    reservation.return_date = datetime.utcnow()
    
    # İlgili ekipmanı tekrar "Mevcut" yap
    if reservation.equipment:
        reservation.equipment.status = 'Mevcut'
        
    db.session.commit()
    flash('Ekipman başarıyla iade edildi.', 'success')
    return redirect(url_for('auth.profile'))

# ---------------------------------------------------------------------------
# API: RESTful endpoint for equipments
# ---------------------------------------------------------------------------
@bp.route('/api/v1/equipments', methods=['GET'])
def api_equipments():
    stmt = db.select(Equipment).order_by(Equipment.id)
    equipments_raw = db.session.execute(stmt).scalars().all()
    
    equipments_data = [
        {
            "id": eq.id,
            "name": eq.name,
            "code": eq.code,
            "laboratory": eq.laboratory,
            "status": eq.status
        }
        for eq in equipments_raw
    ]
    
    return jsonify(equipments_data)
