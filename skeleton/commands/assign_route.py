from commands.base_command import BaseCommand
from core.logistics import Logistics
from core.models_factory import ModelsFactory
from models.vehicle import Vehicle


class AssignRouteToTruck(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        # TODO Add validation for param
        route_id = int(self.params[0])

        return self.logistics.ve
