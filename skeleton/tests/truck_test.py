import unittest

from skeleton.models.constants.vehicle_status import VehicleStatus
from skeleton.models.truck import Truck


class Truck_should(unittest.TestCase):
    def test_valid_initialization(self):
        truck = Truck(1001, "Test", 30000, 5000)
        self.assertEqual(truck.name, "Test")
        self.assertEqual(truck.capacity, 30000)
        self.assertEqual(truck.max_range, 5000)
        self.assertEqual(truck.truck_id, 1001)
        self.assertEqual(truck.status, VehicleStatus.ASSIGNED)
        self.assertEqual(truck.assigned_routes, [])

    def test_name_too_short(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1002, "AB", 40000, 6000)
        self.assertEqual(str(cm.exception), Truck.NAME_ERR)

    def test_name_too_long(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1003, "ThisNameIsTooLong", 40000, 6000)
        self.assertEqual(str(cm.exception), Truck.NAME_ERR)

    def test_capacity_too_low(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1004, "Truck", 5000, 25999)
        self.assertEqual(str(cm.exception), Truck.CAPACITY_ERR)

    def test_capacity_too_high(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1005, "Truck", 70000, 42001)
        self.assertEqual(str(cm.exception), Truck.CAPACITY_ERR)

    def test_range_too_low(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1006, "Truck", 40000, 7999)
        self.assertEqual(str(cm.exception), Truck.RANGE_ERR)

    def test_range_too_high(self):
        with self.assertRaises(ValueError) as cm:
            Truck(1007, "Truck", 40000, 13001)
        self.assertEqual(str(cm.exception), Truck.RANGE_ERR)
