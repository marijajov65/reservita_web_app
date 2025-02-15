from flask import Blueprint, jsonify
from application.models.court import Court
from application.routes.routes_base import RoutesBase
from application.services.schedule_generator import ScheduleGenerator


class CourtRoutes(RoutesBase):

    def __init__(self, schedule_generator: ScheduleGenerator):
        self.schedule_generator = schedule_generator

    def create_blueprint(self) -> Blueprint:
        court_bp = Blueprint('court', __name__)

        @court_bp.route('/all_courts', methods=['GET'])
        def get_courts():
            court_info = self.schedule_generator.get_court_info()
            if court_info:
                return jsonify(court_info)
            return jsonify({'message': 'No court info found'}), 404

        @court_bp.route('/<int:court_id>', methods=['GET'])
        def get_court_by_id(court_id: int):
            court = Court.query.get(court_id)
            if court:
                return jsonify({
                    'id': court.id,
                    'name': court.name,
                    'indoor': court.indoor,
                    'surface': court.surface,
                })
            return jsonify({'message': 'Court not found'}), 404

        return court_bp
