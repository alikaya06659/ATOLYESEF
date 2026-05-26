from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from werkzeug.security import check_password_hash, generate_password_hash

from app import db

# ---------------------------------------------------------------------------
# Model 1: User (Kullanıcı)
# ---------------------------------------------------------------------------

class User(db.Model):
    """Sisteme kayıtlı kullanıcıları temsil eder.

    İlişkiler:
        - User -> Reservation: One-to-Many
    """

    __tablename__ = "user"

    # --- Sütunlar ---
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    username: db.Mapped[str] = db.mapped_column(
        db.String(80), unique=True, nullable=False
    )
    email: db.Mapped[str] = db.mapped_column(
        db.String(120), unique=True, nullable=False
    )
    password_hash: db.Mapped[str] = db.mapped_column(
        db.String(256), nullable=False
    )
    created_at: db.Mapped[datetime] = db.mapped_column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    # --- İlişkiler ---
    reservations: db.Mapped[List["Reservation"]] = db.relationship(
        "Reservation",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
    )

    # --- Parola Yönetimi ---
    def set_password(self, password: str) -> None:
        """Parolayı güvenli bir şekilde hash'ler ve kaydeder."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verilen düz metin parolayı hash ile karşılaştırır."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User id={self.id} username='{self.username}'>"

# ---------------------------------------------------------------------------
# Model 2: Equipment (Ekipman)
# ---------------------------------------------------------------------------

class Equipment(db.Model):
    """Atölye ve laboratuvarlardaki ekipmanları temsil eder.

    Status değerleri: 'Mevcut' | 'Kullanımda' | 'Arızalı'
    """

    __tablename__ = "equipment"

    # Status için geçerli değerler
    VALID_STATUSES = ("Mevcut", "Kullanımda", "Arızalı")

    # --- Sütunlar ---
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(
        db.String(150), nullable=False
    )
    code: db.Mapped[str] = db.mapped_column(
        db.String(50), unique=True, nullable=False
    )
    laboratory: db.Mapped[str] = db.mapped_column(
        db.String(100), nullable=False
    )
    status: db.Mapped[str] = db.mapped_column(
        db.String(20),
        nullable=False,
        default="Mevcut",
        server_default="Mevcut",
    )
    created_at: db.Mapped[datetime] = db.mapped_column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    # --- Tablo seviyesi kısıt (CHECK CONSTRAINT) ---
    __table_args__ = (
        db.CheckConstraint(
            "status IN ('Mevcut', 'Kullanımda', 'Arızalı')",
            name="ck_equipment_status",
        ),
    )

    # --- İlişkiler ---
    reservations: db.Mapped[List["Reservation"]] = db.relationship(
        "Reservation",
        back_populates="equipment",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def __repr__(self) -> str:
        return (
            f"<Equipment id={self.id} code='{self.code}' "
            f"laboratory='{self.laboratory}' status='{self.status}'>"
        )

# ---------------------------------------------------------------------------
# Model 3: Reservation (Rezervasyon / Ödünç Alma)
# ---------------------------------------------------------------------------

class Reservation(db.Model):
    """Bir kullanıcının bir ekipmanı ödünç almasını temsil eder."""

    __tablename__ = "reservation"

    # --- Sütunlar ---
    id: db.Mapped[int] = db.mapped_column(primary_key=True)

    user_id: db.Mapped[int] = db.mapped_column(
        db.ForeignKey("user.id"), nullable=False
    )
    equipment_id: db.Mapped[int] = db.mapped_column(
        db.ForeignKey("equipment.id"), nullable=False
    )

    borrow_date: db.Mapped[datetime] = db.mapped_column(
        db.DateTime, nullable=False
    )
    # return_date: ekipman henüz iade edilmemişse None olabilir
    return_date: db.Mapped[Optional[datetime]] = db.mapped_column(
        db.DateTime, nullable=True
    )

    is_returned: db.Mapped[bool] = db.mapped_column(
        db.Boolean, default=False, nullable=False
    )

    # --- İlişkiler (Many-to-One tarafı) ---
    user: db.Mapped["User"] = db.relationship(
        "User", back_populates="reservations"
    )
    equipment: db.Mapped["Equipment"] = db.relationship(
        "Equipment", back_populates="reservations"
    )

    def __repr__(self) -> str:
        return (
            f"<Reservation id={self.id} user_id={self.user_id} "
            f"equipment_id={self.equipment_id} is_returned={self.is_returned}>"
        )
