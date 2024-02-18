
class DeliveryRoute:
    def __init__(self, route_id):
        self.route_id = route_id
        self.locations = []
        self.route_assigned = False
        self.start_location = None
        self.end_location = None
        self.start_time = None
        self.packages = []

    def add_start_location(self, name, departure_time: str):
        if self.locations:
            raise ValueError("Start location already set")
        self.start_time = departure_time
        self.locations.append({"name": name, "departure_time": departure_time})
        self.start_location = name

    def add_location(self, name, expected_arrival_time: str):
        if not self.locations:
            raise ValueError("Start location must be set first")
        self.locations.append({"name": name, "expected_arrival_time": expected_arrival_time})
        self.end_location = name

    def display_route(self):
        route_info = []
        for i, location in enumerate(self.locations):
            if i == 0:
                route_info.append(f"Start location: {location['name']}, Departure Time: {location['departure_time']}")
            else:
                route_info.append(
                    f"Location {i}: {location['name']}, Expected Arrival Time: {location['expected_arrival_time']}")
        return "\n".join(route_info)


