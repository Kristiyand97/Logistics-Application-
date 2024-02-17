from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory
from datetime import datetime, timedelta


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
        try:
            new_route = self.models_factory.create_route()

            start_name = self.params[0]
            start_departure_time_str = self.params[1] + " " + self.params[2]
            end_name = self.params[3]

            start_departure_time = datetime.strptime(start_departure_time_str, '%d/%m/%y %H:%M')

            # Calculate expected arrival time for the route
            expected_arrival_time = self.logistics.calculate_route_end_time(start_departure_time, start_name, end_name)
            formatted_arrival_time = expected_arrival_time.strftime('%d/%m/%Y %H:%M')
            new_route.add_start_location(start_name, start_departure_time)
            new_route.add_location(end_name, formatted_arrival_time)

            self.logistics.add_route(new_route)
            return f'Route #{new_route.route_id} created'

        except ValueError as e:
            return f"Error: {str(e)}"

