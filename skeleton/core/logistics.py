from datetime import datetime

from skeleton.models.constants.package_status import PackageStatus
from skeleton.models.constants.vehicle_status import VehicleStatus
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

        truck_id = 1001
        for _ in range(10):
            self.unused_vehicles.append(Vehicle(truck_id, "Scania", 4200, 8000))
            truck_id += 1
        for _ in range(15):
            self.unused_vehicles.append(Vehicle(truck_id, "Man", 37000, 10000))
            truck_id += 1
        for _ in range(15):
            self.unused_vehicles.append(Vehicle(truck_id, "Actros", 26000, 13000))
            truck_id += 1

    # def create_package(self, start_location, end_location, weight, customer_contact):
    #     new_package = Package(start_location, end_location, weight, customer_contact)
    #     self.packages.append(new_package)
    #     return new_package

    def add_package(self, package: Package):
        if any(p for p in self.packages if p.id == package.package_id):
            return False
        else:
            self.packages.append(package)
            return True

    # def create_route(self, idx: int):
    #     for route in self.routes:
    #         if idx == route.idx:
    #             raise ValueError(f"Delivery route with ID: {idx} already exists")
    #     new_route = DeliveryRoute(idx, self)
    #     self.routes.append(new_route)
    #     return new_route

    def add_route(self, route: DeliveryRoute):
        if any(r for r in self.routes if r.route_id == route.route_id):
            return False
        else:
            self.routes.append(route)
            return True

    def get_route_by_id(self, route_id: int):
        for route in self.routes:
            if route.route_id == route_id:
                return route
        raise ValueError(f"No route with id: {route_id} exists")

    def get_package_by_id(self, package_id: int):
        for package in self.packages:
            if package.package_id == package_id:
                return package
        raise ValueError(f"No package with id: {package_id} exists")

    def add_start_location_to_route(self, route_id: int, name: str, departure_time: datetime):
        route = self.get_route_by_id(route_id)
        if route:
            route.add_start_location(name, departure_time)
        else:
            raise ValueError(f"No route found with ID: {route_id}")

    def add_location_to_route(self, route_id: int, name: str, arrival_time: datetime):
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

    def calculate_distance(self, route):
        total_distance = 0
        for i in range(len(route.locations) - 1):
            start = route.locations[i]["name"]
            end = route.locations[i + 1]["name"]
            total_distance += self.distances[start][end]
        return total_distance

    def assign_truck_to_route(self, route):
        total_weight = sum(package.weight for package in self.packages if package.assigned_route == route.route_id)
        route_distance = self.calculate_distance(route)

        for truck in self.unused_vehicles:
            if truck.status == VehicleStatus.AVAILABLE and truck.capacity >= total_weight and truck.max_range >= route_distance:
                route.truck = truck.truck_id
                truck.status = VehicleStatus.UNAVAILABLE
                self.unused_vehicles.remove(truck)
                self.used_vehicles.append(truck)
                return f"Truck {truck.name} with ID:{truck.truck_id} was assigned to route {route.route_id}"
        return "No available truck meets the route's requirements"

    def search_route(self, package_id: int):
        package = self.get_package_by_id(package_id)

        valid_routes = []

        for route in self.routes:
            start_index = None
            end_index = None
            for i in range(len(route.locations)):
                if route.locations[i]['name'] == package.start_location:
                    start_index = i
                if route.locations[i]['name'] == package.end_location:
                    end_index = i
            if end_index is not None and start_index is not None and end_index>start_index:
                valid_routes.append(route.display_route())


        if (len(valid_routes) == 0):
            return "No possible routes."
        else:
            return "\n".join(valid_routes)


# logistics = Logistics()
# route_one = logistics.create_route(100)
#
# logistics.add_start_location_to_route(100, "SYD", datetime(2024, 1, 3, 15, 30))
# logistics.add_location_to_route(100, "MEL", datetime(2024, 1, 5, 12, 35))
#
# package_one = logistics.create_package("SYD", "MEL", 45, "Kristiyan")
# print(logistics.assign_package_to_route(package_one, route_one))
# print(logistics.assign_truck_to_route(route_one))
