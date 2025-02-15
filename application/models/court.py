from application import db


class Court(db.Model):
    __tablename__ = 'court'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    indoor = db.Column(db.Boolean())
    surface = db.Column(db.String(20))

    def __repr__(self):
        return (f"Court(id={self.id}, name={self.name}, "
                f"indoor={self.indoor}, surface={self.surface})")

