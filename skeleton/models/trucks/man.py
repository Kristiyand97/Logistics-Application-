from skeleton.models.trucks.vehicle import Truck


class Man(Truck):
    def __init__(self, capacity: int, max_range: int):
        super().__init__("Man", capacity, max_range)


