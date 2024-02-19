from datetime import timedelta, datetime

DISTANCES = {
    "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
    "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
    "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
    "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
    "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
    "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
    "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}
}

AVERAGE_SPEED = 87


def calculate_time_between_cities(start_city: str, end_city: str, departure_time: datetime):
    # Check if departure_time is a valid datetime object
    if not isinstance(departure_time, datetime):
        raise ValueError("Invalid departure time. Must be a datetime object.")

    try:
        # Assuming DISTANCES is a dictionary that provides the distance between cities in kilometers,
        # and AVERAGE_SPEED is the average speed in km/h.
        distance_km = DISTANCES.get(start_city, {}).get(end_city)
        if distance_km is None:
            raise ValueError(f"Distance from {start_city} to {end_city} is not available.")

        travel_time = distance_km / AVERAGE_SPEED
        travel_duration = timedelta(hours=travel_time)

        return departure_time + travel_duration
    except Exception as e:
        print(f"Error calculating time: {e}")
        return None
