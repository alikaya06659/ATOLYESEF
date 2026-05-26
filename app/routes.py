"""
AtölyeŞef — Ana Route Tanımları

Flask Blueprint kullanılmadan, basit fonksiyon tabanlı route'lar.
create_app() içinde 'from app import routes' ile yüklenir.
"""

from flask import current_app as app


@app.route("/")
def index():
    return "Merhaba! AtölyeŞef Ekipman Takip Sistemi'ne hoş geldiniz."


@app.route("/hakkinda")
def hakkinda():
    return """
<h1>Bu bir hakkinda sayfasıdır.</h1>
"""
