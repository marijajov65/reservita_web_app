from datetime import date
from flask import Blueprint, jsonify

from application.routes.routes_base import RoutesBase
from application.services.schedule_generator import ScheduleGenerator


class ScheduleRoutes(RoutesBase):

    def __init__(self, schedule_generator: ScheduleGenerator):
        self._schedule_generator = schedule_generator

    def create_blueprint(self) -> Blueprint:
        schedule_bp = Blueprint('schedule', __name__)

        @schedule_bp.route('/<int:year>/<int:month>/<int:day>', methods=['GET'])
        def get_schedule(year: int, month: int, day: int):
            schedule = self._schedule_generator.get_schedule_for_date(date(year, month, day))
            if schedule:
                return jsonify(
                    schedule
                )
            return jsonify({'message': 'No schedule found'}), 404

        return schedule_bp



