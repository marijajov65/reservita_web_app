import copy

from application.models.court import Court
from application.utils.time_helper import generate_time_array


class ScheduleTemplate:
    def __init__(self):
        self._time_slots = generate_time_array("07:00", "22:30", 30)
        self._generate_template()

    def _generate_template(self):
        courts = Court.query.all()

        self._court_info = [
            {
                "id": court.id,
                "name": court.name,
                "indoor": court.indoor,
                "surface": court.surface,
            }
            for court in courts
        ]

        self._template = [
            {
                "time": time.strftime("%H:%M"),
                **{f"{court.id}": "" for court in courts}
            }
            for time in self._time_slots
        ]

    @property
    def template(self):
        return copy.deepcopy(self._template)

    @property
    def court_info(self):
        return self._court_info
