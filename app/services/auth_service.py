from app.extensions import db
from app.models.user import User
from flask_jwt_extended import create_access_token

def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 0)  # Default to 'user' (0) if no role is provided

    # Ensure role is either 0 (user) or 1 (admin)
    if role not in [0, 1]:
        return {'error': 'Role must be either 0 (user) or 1 (admin)'}, 400

    if not username or not email or not password:
        return {'error': 'All fields are required'}, 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return {'error': 'User already exists'}, 400

    user = User(username=username, email=email, role=role)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 201


def login_user(data):
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return {'error': 'Email and password are required'}, 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return {'error': 'Invalid credentials'}, 401
    access_token = create_access_token(identity={"id": str(user.id), "role": user.role})


    return {'message': f'Welcome {user.username}!', 'access_token': access_token }, 200
