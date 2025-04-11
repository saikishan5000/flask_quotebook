# app/decorators/role_required.py

from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import jsonify
from app.models.user import User  # adjust path if needed

def roles_required(*roles):  # integer roles like 0, 1
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()

            user = User.query.get(user_id)
            if not user or user.role not in roles:
                return jsonify({'error': 'Access forbidden: Insufficient role'}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper
