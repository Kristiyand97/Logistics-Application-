from datetime import datetime, timedelta

from skeleton.models.helper_functions import calculate_time_between_cities, convert_string_to_datetime, \
    calculate_distance


class DeliveryRoute:
    route_id = 1

    def __init__(self, route: str, start_time: datetime):
        self.route_id = DeliveryRoute.route_id
        DeliveryRoute.route_id += 1
        self.locations = route.split(">")
        self.in_progress = False
        self.truck = None
        self.start_time = start_time
        self.current_weight = 0

    def display_route(self):
        if not self.locations or len(self.locations) < 2:
            print("Insufficient locations in the route.")
            return

        # Format the start time
        current_time = self.start_time
        route_information = f"Route ID: {self.route_id} | {self.locations[0].strip()} ({current_time.strftime('%b %dth %H:%Mh')}) "

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
