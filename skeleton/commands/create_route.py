from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory
from datetime import datetime, timedelta


class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], logistics: Logistics, models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        try:
            # Split the first parameter into the route locations
            route_locations = self.params[0].split('>')

            # Parse the departure time
            start_departure_time_str = self.params[1] + " " + self.params[2]
            start_departure_time = datetime.strptime(start_departure_time_str, '%d/%m/%Y %H:%M')

            # Join the locations into a route string
            route_str = '>'.join(route_locations)

            # Create new route using the models factory
            new_route = self.logistics.create_route(route_str, start_departure_time)

            self.logistics.add_route(new_route)
            return f'Route #{new_route.route_id} created'

        except ValueError as e:
            return f"Error: {str(e)}"

