from datetime import timedelta, datetime

from models.constants.constant import DISTANCES, AVERAGE_SPEED, DATE_FORMAT


def calculate_time_between_cities(start_city: str, end_city: str, departure_time: datetime):
    # Assuming DISTANCES is a dictionary that provides the distance between cities in kilometers,
    # and AVERAGE_SPEED is the average speed in km/h.
    distance_km = DISTANCES[start_city][end_city]
    travel_time = distance_km / AVERAGE_SPEED
    travel_duration = timedelta(hours=travel_time)

    # Calculate the arrival time by adding the travel duration to the departure time
    arrival_time = departure_time + travel_duration
    return arrival_time


def convert_string_to_datetime(date_string: str, date_format: str = DATE_FORMAT) -> datetime:
    return datetime.strptime(date_string, date_format)


def calculate_distance(route):
    total_distance = 0
    for i in range(len(route.locations) - 1):
        start = route.locations[i]["name"]
        end = route.locations[i + 1]["name"]
        total_distance += DISTANCES[start][end]
    return total_distance
