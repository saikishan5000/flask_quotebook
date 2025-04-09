# app/services/user_service.py

from app.models.user import User

def get_user_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
