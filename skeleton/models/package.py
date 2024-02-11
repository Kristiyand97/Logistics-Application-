from skeleton.models.constants.constant import PackageStatus


class Package:

    _id = 1

    def __init__(self, start_location: str,
                 end_location: str, weight: float, contact_info):
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        self.status = PackageStatus.PENDING
        self.assigned_route = None
        self.package_id = Package._id
        Package._id += 1

    def assign_route(self, route):
        self.assigned_route = route
        return "A delivery route was assigned to the package"
