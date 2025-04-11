from app import db
from app.models.permission import Permission

def seed_permissions():
    # Predefined permissions
    permissions = ['read', 'write', 'update', 'delete']

    # Check if permissions already exist
    for permission_name in permissions:
        permission = Permission.query.filter_by(name=permission_name).first()
        if not permission:
            # Create new permission
            permission = Permission(name=permission_name)
            db.session.add(permission)
            print(f"Permission '{permission_name}' added.")

    db.session.commit()
    print("Permissions seeded successfully!")

if __name__ == "__main__":
    seed_permissions()
