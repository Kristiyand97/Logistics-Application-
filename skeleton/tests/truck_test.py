import unittest

from skeleton.models.truck import Truck


class Truck_should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act
        truck = Truck(1001, "Scania", 42000, 8000)

        self.assertEquals(truck.truck_id, 1001)
        self.assertEquals(truck.name, "Scania")
        self.assertEquals(truck.capacity, 42000)
        self.assertEquals(truck.max_range, 8000)

    def test_initialization_with_negatives(self):
        # Arrange & Act
        truck = Truck(1002, "Test", -100, -200)

        # Assert
        self.assertGreaterEqual(truck.capacity, 0)
        self.assertGreaterEqual(truck.max_range, 0)

    def test_initialization_with_above_max_capacity_and_range(self):
        # Arrange & Act
        truck = Truck(1001, 'Scania', 42000, 8000)
        large_truck = Truck(1003, "Test", 10000000, 20000000)

        # Assert
        self.assertLessEqual(large_truck.capacity, truck.capacity)
        self.assertLessEqual(large_truck.max_range, truck.max_range)