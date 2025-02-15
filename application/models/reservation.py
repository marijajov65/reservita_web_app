from application import db


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey('court.id'), nullable=False)
    user = db.Column(db.String(40))
    from_time = db.Column(db.Time)
    to_time = db.Column(db.Time)
    reservation_date = db.Column(db.Date)
    details = db.Column(db.String(100))

    def __repr__(self):
        return (f"Reservation(id={self.id}, court_id={self.court_id}, "
                f"user={self.user}, from_time={self.from_time}, "
                f"to_time={self.to_time}, reservation_date={self.reservation_date}, "
                f"details={self.details})")
