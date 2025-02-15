from datetime import datetime

from flask import Blueprint, jsonify, request

from application import db
from application.models.reservation import Reservation
from application.models.schemas.reservation_schema import ReservationSchema
from application.routes.routes_base import RoutesBase


class ReservationRoutes(RoutesBase):

    def __init__(self, reservation_schema: ReservationSchema):
        self._reservation_schema = reservation_schema

    def create_blueprint(self) -> Blueprint:
        reservation_bp = Blueprint('reservation', __name__)

        @reservation_bp.route('/create_reservation', methods=['POST'])
        def create_reservation():
            data = request.get_json()
            errors = self._reservation_schema.validate(data)
            if errors:
                print(errors)
                return jsonify(errors), 403

            try:
                new_reservation = Reservation(
                    court_id=data["court_id"],
                    user=data["name"],
                    from_time=datetime.strptime(data["start_time"], "%H:%M").time(),
                    to_time=datetime.strptime(data["end_time"], "%H:%M").time(),
                    reservation_date=datetime.strptime(data["reservation_date"], "%Y-%m-%d").date(),
                    details=data.get("details", "")
                )

                db.session.add(new_reservation)
                db.session.commit()

                return jsonify({"message": "Reservation saved successfully", "id": new_reservation.id}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        return reservation_bp



