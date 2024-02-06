from skeleton.models.constants.vehicle_status import VehicleStatus


class Vehicle:

    def __init__(self, name: str, capacity: int, max_range: int):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.vehicle_status = VehicleStatus.AVAILABLE







