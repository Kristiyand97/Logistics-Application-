from datetime import datetime, timedelta

from skeleton.models.all_trucks import Trucks
from skeleton.models.constants.constants import DISTANCES
from skeleton.models.constants.package_status import PackageStatus
from skeleton.models.constants.vehicle_status import VehicleStatus
from skeleton.models.package import Package
from skeleton.models.delivery_route import DeliveryRoute


class Logistics:
    def __init__(self):
        self.packages = []
        self.routes = []
        self.valid_routes = []
        self.trucks = Trucks()
        self.distances = DISTANCES

    def add_package(self, package: Package):
        if any(p for p in self.packages if p.id == package.package_id):
            return False
        else:
            self.packages.append(package)
            return True

    def calculate_arrival_time(self, package_id):
        package = next((pkg for pkg in self.packages if pkg.package_id == package_id), None)
        if package is None or package.assigned_route is None:
            return None

        # Find the route the package is assigned to
        route = next((r for r in self.routes if r.route_id == package.assigned_route), None)
        if route is None:
            return f"The package {package}does not have an assigned route yet."

        start_city = package.start_location
        end_city = package.end_location
        departure_time = route.start_time  # Use route's start time

        # Calculate the arrival time
        try:
            distance_km = self.distances[start_city][end_city]
            travel_time = distance_km / 87  # Assuming average speed is 87 km/h
            travel_duration = timedelta(hours=travel_time)
            arrival_time = departure_time + travel_duration
            return arrival_time.strftime('%b %dth %H:%M')
        except KeyError:
            return None  # Distance between cities not found

    def calculate_route_end_time(self, start_time, start_city, end_city):
        if start_city not in self.distances or end_city not in self.distances[start_city]:
            raise ValueError(f"Distance between {start_city} and {end_city} not found")

        distance_km = self.distances[start_city][end_city]
        travel_time = distance_km / 87  # Assuming average speed is 87 km/h
        travel_duration = timedelta(hours=travel_time)
        arrival_time = start_time + travel_duration
        return arrival_time

    def create_package(self, start_location, end_location, weight, contact_info):
        weight = float(weight)  # Ensure weight is a float
        new_package = Package(start_location, end_location, weight, contact_info)
        self.packages.append(new_package)
        return new_package

    def assign_route_to_truck(self, truck_id, route_id):
        truck = self.find_truck_by_id(truck_id)
        route = self.get_route_by_id(route_id)

        if truck is None or route is None:
            return "Truck or route not found."

        if not route.locations or len(route.locations) < 2:
            return "Route does not have enough locations."

        start_location = route.locations[0]["name"]
        end_location = route.locations[-1]["name"]

        if not self.is_truck_available(truck, route.start_time):
            return "Truck is not available for the requested start time."
        truck.status = VehicleStatus.ASSIGNED

        # Calculate end time of the new route
        end_time_of_new_route = self.calculate_route_end_time(route.start_time, start_location, end_location)
        truck.assigned_routes.append((route.route_id, end_time_of_new_route))
        return f"Route {route.route_id} assigned to Truck {truck.truck_id}"

    def is_truck_available(self, truck, start_time):
        if not truck.assigned_routes:
            return True

        last_route_end_time = truck.assigned_routes[-1][1]

        return last_route_end_time <= start_time

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
        raise ValueError(f"No route with id {route_id} exists")

    def get_package_by_id(self, package_id: int):
        for package in self.packages:
            if package.package_id == package_id:
                return package
        raise ValueError(f"No package with id: {package_id} exists")

    def find_truck_by_id(self, truck_id):
        return self.trucks.find_truck_by_id(truck_id)

    def view_package(self, package_id):
        package = self.get_package_by_id(package_id)
        if package:
            print(f"Package ID: {package.package_id}")
            print(f"End Location: {package.end_location}")
            print(f"Weight: {package.weight} kg")
            print(f"Delivery time: {self.calculate_arrival_time(package_id)}")
        else:
            print("Package not found.")

    def calculate_distance(self, route):
        total_distance = 0
        for i in range(len(route.locations) - 1):
            start = route.locations[i]["name"]
            end = route.locations[i + 1]["name"]
            total_distance += self.distances[start][end]
        return total_distance

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
            if end_index is not None and start_index is not None and end_index > start_index:
                valid_routes.append(route.display_route())

        if len(valid_routes) == 0:
            return "No possible routes."
        else:
            self.valid_routes = valid_routes
            return "\n".join(valid_routes)

    def assign_package_to_optimal_route(self, package_id):
        package = self.get_package_by_id(package_id)
        if package is None:
            return "Package not found."

        # Find valid routes using the same logic as search_route
        valid_routes = []
        for route in self.routes:
            start_index = None
            end_index = None
            for i, location in enumerate(route.locations):
                if location['name'] == package.start_location:
                    start_index = i
                if location['name'] == package.end_location:
                    end_index = i
                if end_index is not None and start_index is not None and end_index > start_index:
                    valid_routes.append(route)
                    break

        if not valid_routes:
            return "No suitable route found for the package."

        # Find the shortest route among valid routes
        shortest_route = None
        min_distance = float('inf')
        for route in valid_routes:
            total_distance = self.calculate_distance(route)
            if total_distance < min_distance:
                min_distance = total_distance
                shortest_route = route

        # Assign package to the shortest route
        if shortest_route:
            shortest_route.packages.append(package)
            package.assigned_route = shortest_route.route_id
            package.status = PackageStatus.IN_TRANSIT
            return (f"Package {package_id} with destination {package.end_location} assigned to the shortest route: "
                    f"Route ID: {shortest_route.route_id},Total distance:{total_distance}km.")
        else:
            return "Error in finding the shortest route."
