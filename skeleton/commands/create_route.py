from commands.base_command import BaseCommand
from core.logistics import Logistics
from core.models_factory import ModelsFactory


class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        new_route = self.models_factory.create_route()

        # TODO Add validation for params
        start_name = self.params[0]
        start_departure_time = self.params[1]
        next_name = self.params[2]
        expected_arrival_time = self.params[3]

        new_route.add_start_location(start_name,start_departure_time)
        new_route.add_location(next_name,expected_arrival_time)

        self.logistics.add_route(new_route)

        return f'Route #{new_route.route_id} created'

