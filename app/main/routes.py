from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required
from app import db
from app.main import bp
from app.main.forms import EquipmentForm
from app.models import Equipment

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
