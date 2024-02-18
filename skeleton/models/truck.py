from skeleton.models.constants.vehicle_status import VehicleStatus


class Truck:

    def __init__(self, truck_id: int, name: str, capacity: int, max_range: int):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status = VehicleStatus.ASSIGNED
        self.truck_id = truck_id
        self.assigned_routes = []

    def __str__(self):
        return f"{self.name} | Capacity: {self.capacity} | Max_range: {self.max_range} | ID: {self.truck_id}"
