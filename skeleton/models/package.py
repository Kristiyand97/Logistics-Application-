from skeleton.models.constants.package_status import PackageStatus


class Package:

    START_LOCATION = 3
    END_LOCATION = 3
    LOCATIONS_ERR = "Must be the representative 3 characters for the City. Example: Sydney -> SYD"

    MAX_WEIGHT = 42000
    WEIGHT_ERR = "The truck with maximum capacity is Scania with 42000 kilograms"

    MIN_LEN_CONTACT = 3
    MAX_LEN_CONTACT = 30
    CONTACT_ERR = "The contact information must be betweem 3 and 30 characters"

    id = 1

    def __init__(self, start_location: str,
                 end_location: str, weight: float, contact_info):
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self._contact_info = contact_info
        self.status = PackageStatus.PENDING
        self.assigned_route = None
        self.package_id = Package.id
        Package.id += 1


    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        if value != Package.START_LOCATION:
            raise ValueError(Package.LOCATIONS_ERR)
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        if value != Package.END_LOCATION:
            raise ValueError(Package.LOCATIONS_ERR)
        self._end_location = value


    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > Package.MAX_WEIGHT:
            raise ValueError(Package.WEIGHT_ERR)
        self._weight = value


    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if len(value) < Package.MIN_LEN_CONTACT or len(value) > Package.MAX_LEN_CONTACT:
            raise ValueError(Package.CONTACT_ERR)
        self._contact_info = value


    def assign_route(self, route):
        self.assigned_route = route
        return "A delivery route was assigned to the package"

    def __str__(self):
        return f"{self.package_id} | {self.weight} | {self.contact_info}"
