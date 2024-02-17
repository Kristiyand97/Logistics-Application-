class VehicleStatus:
    ASSIGNED = "Assigned"
    UNASSIGNED = "Unassigned"


    @classmethod
    def from_string(cls, vehicle_status):
        if vehicle_status not in [cls.ASSIGNED, cls.UNASSIGNED]:
            raise ValueError(f'None of the possible status values matches the value {vehicle_status}.')
        return vehicle_status
