from datetime import datetime


class DeliveryRoute:
    def __init__(self, route_id):
        self.route_id = route_id
        self.locations = []
        self.route_assigned = False
        self.truck = None
        self.start_location = None
        self.end_location = None

    def add_start_location(self, name, departure_time: datetime):
        if self.locations:
            raise ValueError("Start location already set")
        if not isinstance(departure_time, datetime):
            raise TypeError("departure_time must be a datetime object")
        self.locations.append({"name": name, "departure_time": departure_time})
        self.start_location = name

    def add_location(self, name, expected_arrival_time: datetime):
        if not self.locations:
            raise ValueError("Start location must be set first")
        if not isinstance(expected_arrival_time, datetime):
            raise TypeError("expected_arrival_time must be datetime object")
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



