import pinject


class AppBindings(pinject.BindingSpec):

    def configure(self, bind):
        from application.services.schedule_template import ScheduleTemplate
        bind("schedule_template", to_class=ScheduleTemplate)

        from application.services.schedule_generator import ScheduleGenerator
        bind("schedule_generator", to_class=ScheduleGenerator)

        # Schemas
        from application.models.schemas.reservation_schema import ReservationSchema
        bind("reservation_schema", to_class=ReservationSchema)

        # Blueprints
        from application.routes.schedule_routes import ScheduleRoutes
        bind("schedule_routes", to_class=ScheduleRoutes)

        from application.routes.court_routes import CourtRoutes
        bind("court_routes", to_class=CourtRoutes)

        from application.routes.reservation_routes import ReservationRoutes
        bind("reservation_routes", to_class=ReservationRoutes)


