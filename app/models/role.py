from app.extensions import db
from app.models.associations import role_permissions
from app.models.permission import Permission

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    permissions = db.relationship('Permission', secondary=role_permissions, backref='roles')

    def __repr__(self):
        return f"<Role {self.name}>"
