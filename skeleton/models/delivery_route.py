from datetime import datetime

from skeleton.models.constants.constants import calculate_time_between_cities


class DeliveryRoute:
    route_id = 1
    #S
    def __init__(self, route: str, start_time: datetime):
        self.route_id = DeliveryRoute.route_id
        DeliveryRoute.route_id += 1
        self.locations = route.split(">")
        self.in_progress = "Not in progress"
        self.truck = None
        self.start_time = start_time
        self.packages = []

    def display_route(self):
        if not self.locations or len(self.locations) < 2:
            return "Insufficient locations in the route."

        # Format the start time
        current_time = self.start_time
        route_information = f"{self.locations[0].strip()} ({current_time.strftime('%b %dth %H:%Mh')}) "

        # Iterate over the locations
        for i in range(1, len(self.locations)):
            # Calculate the arrival time at the next location
            current_time = calculate_time_between_cities(
                self.locations[i - 1].strip(),
                self.locations[i].strip(),
                current_time
            )

            # Add the location and its formatted arrival time to the route information
            route_information += f" → {self.locations[i].strip()} ({current_time.strftime('%b %dth %H:%Mh')})"

        return route_information
