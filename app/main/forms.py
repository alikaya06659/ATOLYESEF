from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class EquipmentForm(FlaskForm):
    """Ekipman ekleme ve güncelleme formu.
    Kullanıcıdan name, code, laboratory ve status bilgilerini alır.
    """
    name = StringField(
        "Ekipman Adı",
        validators=[DataRequired(message="Lütfen ekipman adını giriniz."), Length(max=150)],
    )
    code = StringField(
        "Kod",
        validators=[DataRequired(message="Kod gerekli."), Length(max=50)],
    )
    laboratory = StringField(
        "Laboratuvar",
        validators=[DataRequired(message="Laboratuvar adı gerekli."), Length(max=100)],
    )
    status = SelectField(
        "Durum",
        choices=[
            ("Mevcut", "Mevcut"),
            ("Kullanımda", "Kullanımda"),
            ("Arızalı", "Arızalı"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Kaydet")
