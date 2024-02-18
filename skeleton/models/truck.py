from skeleton.models.constants.vehicle_status import VehicleStatus


class Truck:
    MIN_LEN_NAME = 3
    MAX_LEN_NAME = 10
    NAME_ERR = f"The range must be between {MIN_LEN_NAME} and {MAX_LEN_NAME}"

    MIN_CAPACITY = 10000
    MAX_CAPACITY = 60000
    CAPACITY_ERR = f"The range must be between {MIN_CAPACITY} and {MAX_CAPACITY}"

    MIN_RANGE = 1000
    MAX_RANGE = 10000
    RANGE_ERR = f"The range must be between {MIN_RANGE} and {MAX_RANGE}"

    def __init__(self, truck_id: int, name: str, capacity: int, max_range: int):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status = VehicleStatus.ASSIGNED
        self.truck_id = truck_id
        self._assigned_routes = []

    @property
    def assigned_routes(self):
        return tuple(self._assigned_routes)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < Truck.MIN_LEN_NAME or len(value) > Truck.MAX_LEN_NAME:
            raise ValueError(Truck.NAME_ERR)
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < Truck.MIN_CAPACITY or value > Truck.MAX_CAPACITY:
            raise ValueError(Truck.CAPACITY_ERR)
        self._capacity = value

    @property
    def max_range(self):
        return self._max_range

    @max_range.setter
    def max_range(self, value):
        if value < Truck.MIN_RANGE or value > Truck.MAX_RANGE:
            raise ValueError(Truck.RANGE_ERR)
        self._max_range = value

    def __str__(self):
        return f"{self.name} | Capacity: {self.capacity} | Max_range: {self.max_range} | ID: {self.truck_id}"
