from models.package import Package


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


