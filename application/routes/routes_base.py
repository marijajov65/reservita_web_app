from abc import ABC, abstractmethod
from flask import Blueprint


class RoutesBase(ABC):
    @abstractmethod
    def create_blueprint(self) -> Blueprint:
        pass
