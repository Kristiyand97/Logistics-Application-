from datetime import datetime

from skeleton.models.constants.package_status import PackageStatus
from skeleton.models.package import Package
from skeleton.models.delivery_route import DeliveryRoute
from skeleton.models.vehicle import Vehicle


class Logistics:
    def __init__(self):
        self.packages = []
        self.routes = []
        self.unused_vehicles = []
        self.used_vehicles = []
        self.distances = {
            "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
            "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
            "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
            "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
            "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
            "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
            "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}
        }

        for truck_id in range(1001, 1011):
            self.unused_vehicles.append(Vehicle("Scania", 4200, 8000))
        for truck_id in range(1011, 2026):
            self.unused_vehicles.append(Vehicle("Man", 37000, 10000))
        for truck_id in range(1026, 1041):
            self.unused_vehicles.append(Vehicle("Actros", 26000, 13000))

    def create_package(self, start_location, end_location, weight, customer_contact):
        new_package = Package(start_location, end_location, weight, customer_contact)
        self.packages.append(new_package)
        return new_package

    def create_route(self, idx: int):
        for route in self.routes:
            if idx == route.idx:
                raise ValueError(f"Delivery route with ID: {idx} already exists")
        new_route = DeliveryRoute(idx)
        self.routes.append(new_route)
        return new_route

    def get_route_by_id(self, route_id: int):
        for route in self.routes:
            if route.route_id == route_id:
                return route
        raise ValueError(f"No route with id: {route_id} exists")

    def add_start_location_to_route(self, route_id: int, name: str, departure_time: datetime):
        route = self.get_route_by_id(route_id)
        if route:
            route.add_start_location(name, departure_time)
        else:
            raise ValueError(f"No route found with ID: {route_id}")

    def add_location_to_route(self, route_id, name, arrival_time: datetime):
        route = self.get_route_by_id(route_id)
        if route:
            route.add_location(name, arrival_time)
        else:
            raise ValueError(f"No route found with ID: {route_id}")

    def assign_package_to_route(self, package, route):
        for r in self.routes:
            if r.route_id == route.route_id:
                if package.start_location == r.start_location and package.end_location == r.end_location:
                    package.assign_route(route)
                    package.assigned_route = route.route_id
                    route.route_assigned = True
                    return f"Package was successfully added to route with ID: {route.route_id}"


logistics = Logistics()
route_one = logistics.create_route(100)

logistics.add_start_location_to_route(100, "SYD", datetime(2024, 1, 3, 15, 30))
logistics.add_location_to_route(100, "MEL", datetime(2024, 1, 5, 12, 35))

package_one = logistics.create_package("SYD", "MEL", 45, "Kristiyan")

print(logistics.assign_package_to_route(package_one, route_one))


