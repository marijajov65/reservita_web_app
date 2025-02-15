from marshmallow import Schema, fields


class ReservationSchema(Schema):
    court_id = fields.Int(required=True)
    reservation_date = fields.Date(required=True)
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)
    name = fields.Str(required=True)
    details = fields.Str()
