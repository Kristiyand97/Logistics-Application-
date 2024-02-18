import unittest

from skeleton.models.all_trucks import Trucks


class Trucks_should(unittest.TestCase):
    def test_singelton_pattern(self):
        trucks1 = Trucks()
        trucks2 = Trucks()

        self.assertIs(trucks1, trucks2)

    def test_initialization(self):
        trucks = Trucks()

        self.assertEqual(len(trucks.trucks), 40)

    def test_find_truck_by_id(self):
        trucks = Trucks()
        truck_id = 1001
        found_truck = trucks.find_truck_by_id(truck_id)

        self.assertIsNotNone(found_truck)
        self.assertEqual(found_truck.truck_id, truck_id)
