from datetime import datetime

class DeliveryRoute:
    def __init__(self, route_id):
        # self.logistics = logistics
        self.route_id = route_id
        self.locations = []
        self.route_assigned = False
        self.truck = None
        self.start_location = None
        self.end_location = None

    def add_start_location(self, name, departure_time: str):
        if self.locations:
            raise ValueError("Start location already set")
        if not isinstance(departure_time, str):
            raise TypeError("departure_time must be a str object")
        self.locations.append({"name": name, "departure_time": datetime.strptime(departure_time, "%d/%m/%y%H:%M")})
        self.start_location = name

    def add_location(self, name, expected_arrival_time: str):
        if not self.locations:  raise ValueError("Start location must be set first")
        if not isinstance(expected_arrival_time, str):
            raise TypeError("expected_arrival_time must be str object")
        self.locations.append({"name": name, "expected_arrival_time": datetime.strptime(expected_arrival_time, "%d/%m/%y%H:%M")})
        self.end_location = name


    def calculate_arrival_times(self, route):
        average_speed = 87
        if not self.locations or len(self.locations) < 2:
            raise ValueError("Not enough locations to calculate arrival time")
        for i in range(1, len(self.locations)):
            raise NotImplementedError('Possibly implement in logistics')
            # distance = self.logistics.calculate_distance(route)
            # NOT FINISHED

    def display_route(self):
        route_info = []
        for i, location in enumerate(self.locations):
            if i == 0:
                route_info.append(f"Start location: {location['name']}, Departure Time: {location['departure_time']}")
            else:
                route_info.append(
                    f"Location {i}: {location['name']}, Expected Arrival Time: {location['expected_arrival_time']}")
        return "\n".join(route_info)
