from . import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<URL {self.short_url} -> {self.original_url}>'