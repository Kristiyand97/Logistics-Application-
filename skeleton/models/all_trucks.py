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
        self.trucks = []
        self._initialized = True
        self.generate_trucks()

    def generate_trucks(self):
        """
        This method creates all the trucks once it is called.
        """
        truck_id = 1001
        for _ in range(10):
            self.trucks.append(Truck(truck_id, "Scania", 4200, 8000))
            truck_id += 1
        for _ in range(15):
            self.trucks.append(Truck(truck_id, "Man", 37000, 10000))
            truck_id += 1
        for _ in range(15):
            self.trucks.append(Truck(truck_id, "Actros", 26000, 13000))
            truck_id += 1

    def find_suitable_truck(self, max_range: int) -> Truck:
        for truck in self.trucks:
            if truck.max_range >= max_range:
                return truck

    def find_truck_by_id(self, truck_id: int):
        # Search in unused trucks
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck

        # Search in used trucks
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
