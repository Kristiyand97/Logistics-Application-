class VehicleStatus:
    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"

    @classmethod
    def from_string(cls, vehicle_status):
        if vehicle_status not in [cls.AVAILABLE, cls.UNAVAILABLE]:
            raise ValueError(f'None of the possible status values matches the value {vehicle_status}.')
        return vehicle_status


