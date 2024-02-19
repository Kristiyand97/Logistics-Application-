from datetime import datetime, timedelta
from skeleton.models.all_trucks import Trucks
from skeleton.models.constants.constants import DISTANCES, calculate_time_between_cities, AVERAGE_SPEED
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
        if package is None:
            return None

        # Find the route the package is assigned to
        route = next((r for r in self.routes if r.route_id == package.assigned_route), None)
        if route is None:
            return f"The package {package_id} does not have an assigned route yet."

        if not route.locations or package.end_location not in route.locations:
            return "The destination of the package is not on the assigned route."

        current_time = route.start_time  # Use route's start time

        for i in range(1, len(route.locations)):
            if route.locations[i - 1].strip() == package.start_location and route.locations[
                i].strip() == package.end_location:
                current_time = calculate_time_between_cities(
                    route.locations[i - 1].strip(),
                    route.locations[i].strip(),
                    current_time
                )
                return current_time

        return "Could not calculate arrival time."

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
        route = self.get_delivery_route(route_id)

        if truck is None or route is None:
            return "Truck or route not found."

        if not route.locations or len(route.locations) < 2:
            return "Route does not have enough locations."

        if not self.is_truck_available(truck, route.start_time):
            return "Truck is not available for the requested start time."

        truck.status = VehicleStatus.ASSIGNED

        # Update the in_progress attribute of the route
        route.in_progress = "In progress"  # This line is modified

        # Calculate end time of the new route and update the truck's assigned routes
        end_time_of_new_route = self.calculate_route_end_time(route.start_time, route.locations[0], route.locations[-1])
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

    def get_delivery_route(self, route_id: int):
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
            start = route.locations[i]
            end = route.locations[i + 1]
            total_distance += self.distances[start][end]
        return total_distance

    def search_route(self, package_id: int):
        package = self.get_package_by_id(package_id)

        if package is None:
            return "Package not found."

        valid_routes = []

        for route in self.routes:
            start_index = None
            end_index = None
            for i, location in enumerate(route.locations):
                if location.strip() == package.start_location:
                    start_index = i
                if location.strip() == package.end_location:
                    end_index = i
                if end_index is not None and start_index is not None and end_index > start_index:
                    break  # Exit loop as soon as both start and end indices are found

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
                if location.strip() == package.start_location:
                    start_index = i
                if location.strip() == package.end_location:
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

    def create_route(self, route: str, start_time) -> DeliveryRoute:
        if route in self.routes:
            raise ValueError(f"Delivery route already exists")
        new_route = DeliveryRoute(route, start_time)
        self.routes.append(new_route)
        return new_route

    def estimate_travel_time(self, route):
        total_distance = self.calculate_distance(route)
        if total_distance is None:
            return "Cannot estimate travel time: distance information is missing."

        # Calculate travel time in hours
        travel_time_hours = total_distance / AVERAGE_SPEED

        # Convert to a timedelta for easy formatting and manipulation
        travel_duration = timedelta(hours=travel_time_hours)

        return travel_duration
