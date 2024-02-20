from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory

#S
class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        route_id = int(self.params[0])
        route = self.logistics.get_delivery_route(route_id)

        if route:
            route_info = [
                f"Route ID: {route.route_id}",
                f"Status: {route.in_progress}",
            ]

            if route.truck:
                route_info.append(f"Assigned Truck: {route.truck.truck_id}")  # Assuming truck has a truck_id attribute

            # Modify display_route to return the route information as a string
            route_information = route.display_route()
            if route_information:
                route_info.append(route_information)

            if route.in_progress:
                estimated_travel_time = self.logistics.estimate_travel_time(route)
                # Convert timedelta to hours and minutes
                hours, remainder = divmod(estimated_travel_time.total_seconds(), 3600)
                minutes = remainder // 60
                travel_time_str = f"{int(hours)}h {int(minutes)}m"
                route_info.append(f"Estimated Travel Time: {travel_time_str}")

            return "\n".join(route_info)
        else:
            return "Route not found."
