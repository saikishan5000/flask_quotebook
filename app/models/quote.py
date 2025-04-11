from app.extensions import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    quote = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "quote": self.quote
        }
