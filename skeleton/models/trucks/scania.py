from skeleton.models.trucks.vehicle import Vehicle


class Scania(Vehicle):
    idx = 1

    def __init__(self, capacity: int, max_range: int):
        super().__init__("Scania", capacity, max_range)
        self.idx = Scania.idx
        Scania.idx += 1



