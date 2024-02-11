from datetime import datetime

from skeleton.models import package
from skeleton.models.constants.constant import DISTANCES, PackageStatus, VehicleStatus
from skeleton.models.helper_functions import calculate_distance
from skeleton.models.package import Package
from skeleton.models.delivery_route import DeliveryRoute
from skeleton.models.packages import Packages
from skeleton.models.truck import Truck
from skeleton.models.trucks import Truck, Trucks
from skeleton.models.all_routes import AllRoutes


class Logistics:
    def __init__(self):
        self.packages = Packages()
        self.routes = AllRoutes()
        self.trucks = Trucks()
        self.distances = DISTANCES

    def create_package(self, start_location, end_location, weight, customer_contact):
        new_package = Package(start_location, end_location, weight, customer_contact)
        self.packages[new_package.package_id] = new_package
        return new_package

    def find_route_suitable_for_package(self, package: Package) -> str:
        available_routes: list[DeliveryRoute] = []
        for delivery_route_key, delivery_route_value in self.routes.delivery_routes:
            route: DeliveryRoute = delivery_route_value
            locations: list[str] = route.locations

            # The below variable is used to ensure the end_location is only
            # confirmed when there is a start_location found before that.
            is_start_location_found = False

            for location in locations:
                if package.start_location == location:
                    is_start_location_found = True
                    continue
                if package.end_location == location and is_start_location_found:
                    available_routes.append(delivery_route_value)
                    break

        return "\n".join([available_route.display_route() for available_route in available_routes])

    def create_route(self, route: str, start_time) -> DeliveryRoute:
        if route in self.routes:
            raise ValueError(f"Delivery route already exists")
        new_route = DeliveryRoute(route, start_time)
        self.routes = new_route
        return new_route

    def assign_truck_to_route_by_distance(self, route_id):
        route: DeliveryRoute = self.routes.get_route_by_id(route_id)
        route_distance = calculate_distance(route_id)
        route.truck = self.trucks.find_suitable_truck(route_distance)

    def assign_truck_to_route_by_weight(self, route_id):
        # TODO to be finished
        pass

