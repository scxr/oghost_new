from functools import wraps
from flask import abort
from flask_jwt_extended import get_jwt_identity
from app.main.config.models import User

def admin_required(function):
    '''
    this decorator should be called after @jwt_required
    '''
    @wraps(function)
    def decorated_view(*args, **kwargs):
        username = get_jwt_identity()
        current_user = User.query.filter_by(username=username).first()
        if current_user.is_superuser:
            return function(*args, **kwargs)
        else:
            return abort(404)
    return decorated_view