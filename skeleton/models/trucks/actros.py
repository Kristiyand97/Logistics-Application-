from skeleton.models.trucks.vehicle import Truck


class Actros(Truck):
    def __init__(self, capacity: int, max_range: int):
        super().__init__("Actros", capacity, max_range)
