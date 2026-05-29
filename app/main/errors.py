from flask import render_template
from app.main import bp

from werkzeug.exceptions import HTTPException

@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    # Pass through standard HTTP errors (404, 403, 405, etc.)
    from app import db
    if e.code == 500:
        db.session.rollback()
        
    return render_template('errors/error.html', error=e), e.code

@bp.app_errorhandler(Exception)
def handle_unexpected_error(e):
    # Catch any unexpected code bugs that crash the server (converts to 500)
    from app import db
    db.session.rollback()
    
    class DummyError:
        code = 500
        name = "İç Sunucu Hatası"
        description = "Sistemde beklenmeyen kritik bir arıza oluştu."
        
    return render_template('errors/error.html', error=DummyError()), 500
