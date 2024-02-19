from skeleton.models.delivery_route import DeliveryRoute
from skeleton.models.truck import Truck


class ModelsFactory:
    def __init__(self):
        self._route_id = 1
        self._truck_id = 1001


    def generate_truck(self, name: str, capacity: int, max_range: int):
        truck_id = self._truck_id
        self._truck_id += 1
        return Truck(truck_id, name, capacity, max_range)
