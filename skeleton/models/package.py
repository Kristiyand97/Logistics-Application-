from skeleton.models.constants.constant import PackageStatus
from skeleton.models.helper_functions import calculate_time_between_cities


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
            estimated_arrival_time = calculate_time_between_cities()
            package_info += f"Estimated Arrival Time: {estimated_arrival_time.strftime('%b %d %H:%M')}\n"
        else:
            package_info += "Not yet assigned to a route\n"

        return package_info

