from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(40))

    def __repr__(self):
        return f"<User {self.name}>"
