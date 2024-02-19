from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory


#S
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
        # Validate the parameters
        if len(self.params) < 2 or not self.params[0].isdigit() or not self.params[1].isdigit():
            return "Invalid input. Please provide a valid route ID and truck ID."

        route_id = int(self.params[0])
        truck_id = int(self.params[1])

        # Call the Logistics method to assign the route to the truck
        assignment_result = self.logistics.assign_route_to_truck(truck_id, route_id)
        return assignment_result
