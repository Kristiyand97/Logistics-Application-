from datetime import timedelta, datetime

from skeleton.models.constants.constant import DISTANCES, AVERAGE_SPEED, DATE_FORMAT
from skeleton.models.packages import Packages


def calculate_time_between_cities(start_city: str, end_city: str, departure_time: datetime):
    # Assuming DISTANCES is a dictionary that provides the distance between cities in kilometers,
    # and AVERAGE_SPEED is the average speed in km/h.
    distance_km = DISTANCES[start_city][end_city]
    travel_time = distance_km / AVERAGE_SPEED
    travel_duration = timedelta(hours=travel_time)

    # Calculate the arrival time by adding the travel duration to the departure time
    arrival_time = departure_time + travel_duration
    return arrival_time


# from datetime import datetime, timedelta
#
# # Example datetime objectcurrent_datetime = datetime.now()
#
# # Add hours to the datetimehours_to_add = 3  # For example, add 3 hoursnew_datetime = current_datetime + timedelta(hours=hours_to_add)
#
# print("Original datetime:", current_datetime)print("New datetime after adding 3 hours:", new_datetime)
#

def calculate_arrival_time_for_package(package_id: int):
    package = Packages.find_package_by_id(package_id)  # Replace with actual way to retrieve the package

    if not package or not package.assigned_route:
        raise ValueError("Package not found or not assigned to a route")

    departure_time = package.assigned_route.start_time
    current_time = departure_time

    # Iterate over the route locations until the package's end location is reached
    for i in range(len(package.assigned_route.locations) - 1):
        start_city = package.assigned_route.locations[i].strip()
        end_city = package.assigned_route.locations[i + 1].strip()

        if start_city == package.end_location:
            break

        current_time = calculate_time_between_cities(start_city, end_city, current_time)

        if end_city == package.end_location:
            break

    return current_time



# def calculate_arrival_time(self, package_id):
#
#     package = next((pkg for pkg in self.packages if pkg.package_id == package_id), None)
#
#     if package is None:
#         return None
#
#     start_city = package.start_location
#     end_city = package.end_location
#
#     # departure_time = datetime.strptime(DeliveryRoute.start_location, '%Y-%m-%d %H:%M')
#
#     # Calculate the arrival time
#     try:
#         distance_km = self.distances[(start_city, end_city)]
#         travel_time = distance_km / 87
#         travel_duration = timedelta(hours=travel_time)
#         # arrival_time = departure_time + travel_duration
#         return arrival_time
#     except KeyError:
#         return None  # Distance between the cities not found





def convert_string_to_datetime(date_string: str, date_format: str = DATE_FORMAT) -> datetime:
    return datetime.strptime(date_string, date_format)


def calculate_distance(route):
    total_distance = 0
    for i in range(len(route.locations) - 1):
        start = route.locations[i]["name"]
        end = route.locations[i + 1]["name"]
        total_distance += DISTANCES[start][end]
    return total_distance