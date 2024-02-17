from skeleton.models.constants.vehicle_status import VehicleStatus


class Vehicle:

    def __init__(self, truck_id: int, name: str, capacity: int, max_range: int):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status = VehicleStatus.AVAILABLE
        self.truck_id = truck_id
        self.assigned_routes = []
