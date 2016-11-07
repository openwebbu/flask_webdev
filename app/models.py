from app import db

# Stick to these table columns for now
class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    cuisine = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Name: %r, Cuisine: %r>' % (self.name, self.cuisine)
        
    def __str__(self):
        return self.name