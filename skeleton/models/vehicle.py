class Vehicle:

    id = 1001

    def __init__(self, name, capacity, max_range):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status = "Available"
        self.vehicle_id = Vehicle.id
        Vehicle.id += 1