from skeleton.models.delivery_route import DeliveryRoute
from skeleton.models.package import Package
from skeleton.models.truck import Truck


class ModelsFactory:
    def __init__(self):
        self._route_id = 1
        self._truck_id = 1001

    def create_route(self):
        route_id = self._route_id
        self._route_id += 1
        return DeliveryRoute(route_id)

    def generate_truck(self, name: str, capacity: int, max_range: int):
        truck_id = self._truck_id
        self._truck_id += 1
        return Truck(truck_id, name, capacity, max_range)
