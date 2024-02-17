from skeleton.models.constants.package_status import PackageStatus


class Package:

    id = 1

    def __init__(self, start_location: str,
                 end_location: str, weight: float, contact_info):
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        self.status = PackageStatus.PENDING
        self.assigned_route = None
        self.package_id = Package.id
        Package.id += 1
        # print(f"Creating package with ID: {Package.id}")
    def assign_route(self, route):
        self.assigned_route = route
        return "A delivery route was assigned to the package"

    def __str__(self):
        return f"{self.package_id} | {self.weight} | {self.contact_info}"








