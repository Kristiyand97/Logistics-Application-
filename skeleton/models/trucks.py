from skeleton.models.truck import Truck


class Trucks:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Trucks, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.used_trucks = []
        self.unused_trucks = []
        self._initialized = True
        self.generate_trucks()

    def generate_trucks(self):
        """
        This method creates all the trucks once it is called.
        """
        truck_id = 1001
        for _ in range(10):
            self.unused_trucks.append(Truck(truck_id, "Scania", 4200, 8000))
            truck_id += 1
        for _ in range(15):
            self.unused_trucks.append(Truck(truck_id, "Man", 37000, 10000))
            truck_id += 1
        for _ in range(15):
            self.unused_trucks.append(Truck(truck_id, "Actros", 26000, 13000))
            truck_id += 1

    def change_to_used(self, truck_id: int):
        """
        Once a truck is assigned to a route, the truck is moved from
        unused_trucks list to used_trucks list until the package is delivered.
        :param truck_id: int
        """
        truck = next(truck for truck in self.unused_trucks if truck.truck_id == truck_id)
        self.unused_trucks.remove(truck)
        self.used_trucks.append(truck)

    def change_to_unused(self, truck_id: int):
        """
        Once a package is delivered, the truck is removed from used_trucks, and
        it is moved back to unused_trucks waiting for another route and package to be assigned to.
        :param truck_id: int
        """
        truck = next(truck for truck in self.used_trucks if truck.truck_id == truck_id)
        self.used_trucks.remove(truck)
        self.unused_trucks.append(truck)

    def find_suitable_truck(self, max_range: int) -> Truck:
        for truck in self.unused_trucks:
            if truck.max_range >= max_range:
                self.change_to_used(truck.truck_id)
                return truck


