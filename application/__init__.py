import pinject
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from application.bindings.app_bindings import AppBindings
from config import Config


db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from application.routes.court_routes import CourtRoutes
        from application.routes.schedule_routes import ScheduleRoutes
        from application.routes.reservation_routes import ReservationRoutes

        CORS(app)
        obj_graph = pinject.new_object_graph(binding_specs=[AppBindings()])
        schedule_routes = obj_graph.provide(ScheduleRoutes)
        court_routes = obj_graph.provide(CourtRoutes)
        reservation_routes = obj_graph.provide(ReservationRoutes)

        app.register_blueprint(schedule_routes.create_blueprint(), url_prefix="/schedule")
        app.register_blueprint(court_routes.create_blueprint(), url_prefix="/courts")
        app.register_blueprint(reservation_routes.create_blueprint(), url_prefix="/reservation")

        return app
