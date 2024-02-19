class PackageStatus:
    PENDING = "Pending"
    IN_TRANSIT = "In transit"
    DELIVERED = "Delivered"

    @classmethod
    def from_string(cls, status_string):
        if status_string not in [cls.PENDING, cls.IN_TRANSIT, cls.DELIVERED]:
            raise ValueError(f'None of the possible status values matches the value {status_string}.')
        return status_string

