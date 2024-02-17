from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory


class ViewTruckCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        truck_id = int(self.params[0])
        truck = self.logistics.find_truck_by_id(truck_id)

        if truck:
            truck_info = [
                f"Truck ID: {truck.truck_id}",
                f"Name: {truck.name}",
                f"Capacity: {truck.capacity}",
                f"Max Range: {truck.max_range}",
                f"Status: {truck.status}"
            ]

            if truck.assigned_routes:
                truck_info.append("Assigned Routes:")
                for route_id, end_time in truck.assigned_routes:
                    truck_info.append(f"  - Route ID: {route_id}, Arrival Time: {end_time.strftime('%b %dth %H:%M')}")
            else:
                truck_info.append("No routes assigned.")

            return "\n".join(truck_info)
        else:
            return "Truck not found."
