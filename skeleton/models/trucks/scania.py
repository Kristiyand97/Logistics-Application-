from skeleton.models.trucks.truck import Truck


class Scania(Truck):
    def __init__(self, capacity: int(4200), max_range: int(8000)):
        super().__init__("Scania", capacity, max_range)

