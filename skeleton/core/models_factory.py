from models.delivery_route import DeliveryRoute
from models.package import Package


class ModelsFactory:
    def __init__(self):
        self._route_id = 1

    def create_route(self):
        route_id = self._route_id
        self._route_id += 1
        return DeliveryRoute(route_id)

    def create_package(self, start_location: str, end_location: str, weight: str, contact_info):
        weight = float(weight)

        return Package(start_location, end_location, weight, contact_info)
