from skeleton.models.helper_functions import calculate_time_between_cities
from skeleton.models.package import Package


class Packages:
    def __init__(self):
        self._packages = {}

    @property
    def packages(self):
        return tuple(self._packages)

    @staticmethod
    def assign_package_to_route(package: Package, route_id: int):
        if package.assigned_route:
            raise ValueError(f"Package already assigned to route id: {route_id}")
        package.assigned_route = route_id

    def find_package_by_id(self, package_id) -> Package:
        return self._packages.get(package_id)

    def add_package(self, package_id, package):
        self._packages[package_id] = package

    def get_package(self, package_id):
        return self._packages.get(package_id)

    def display_package(self):
        package_info = (
            f"Package ID: {self.package_id}\n"
            f"Start Location: {self.start_location}\n"
            f"End Location: {self.end_location}\n"
            f"Weight: {self.weight} kg\n"
            f"Contact Info: {self.contact_info}\n"
            f"Status: {self.status}\n"
        )

        if self.assigned_route:
            package_info += f"Assigned to route ID: {self.assigned_route.route_id}\n"
            estimated_arrival_time = self.estimate_arrival_time()
            package_info += f"Estimated Arrival Time: {estimated_arrival_time.strftime('%b %d %H:%M')}\n"
        else:
            package_info += "Not yet assigned to a route\n"

        print(package_info)