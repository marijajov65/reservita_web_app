from datetime import datetime

from application.models.reservation import Reservation
from application.services.schedule_template import ScheduleTemplate


class ScheduleGenerator:
    def __init__(self, schedule_template: ScheduleTemplate):
        self._schedule_template = schedule_template

    def get_court_info(self):
        return self._schedule_template.court_info

    def get_schedule_for_date(self, reservation_date: datetime.date):
        reservations = Reservation.query.filter_by(reservation_date=reservation_date).all()
        schedule = self._schedule_template.template

        for slot in schedule:
            for reservation in reservations:
                if reservation.from_time <= datetime.strptime(slot['time'], "%H:%M").time() < reservation.to_time:
                    court_key = f"{reservation.court_id}"
                    if court_key in slot:
                        slot[court_key] = reservation.user

        return schedule
