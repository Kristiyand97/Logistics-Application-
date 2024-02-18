import unittest
from unittest import TestCase
from skeleton.models.package import Package

v_start_loc = "SYD"
v_end_loc = "BRI"
v_weight = 200
v_contact_info = "0898967597"


class Package_Should(unittest.TestCase):

    def test_package_assignValues(self):
        package1 = Package(v_start_loc, v_end_loc, v_weight, v_contact_info)

        self.assertEqual(v_start_loc, package1.start_location)
        self.assertEqual(v_end_loc, package1.end_location)
        self.assertEqual(v_weight, package1.weight)
        self.assertEqual(v_contact_info, package1.contact_info)

    def test_package_raiseError_invalid_start_location(self):
        with self.assertRaises(ValueError):
            Package("AD", v_end_loc, v_weight, v_contact_info)

    def test_package_raiseError_invalid_end_location(self):
        with self.assertRaises(ValueError):
            Package(v_start_loc, "AD", v_weight, v_contact_info)

    def test_package_raiseError_invalid_weight(self):
        with self.assertRaises(ValueError):
            Package(v_start_loc, v_end_loc, 0, v_contact_info)

    def test_package_raiseError_invalid_contact_info(self):
        with self.assertRaises(ValueError):
            Package(v_start_loc, v_end_loc, v_weight, "")

    def test_displayPackage_no_assigned_route(self):
        package1 = Package(v_start_loc, v_end_loc, v_weight, v_contact_info)
        expected = (
            f"Package ID: {package1.package_id}\n"
            f"Start Location: {v_start_loc}\n"
            f"End Location: {v_end_loc}\n"
            f"Weight: {v_weight} kg\n"
            f"Contact Info: {v_contact_info}\n"
            f"Status: {package1.status}\n"
        )

        actual = package1.display_package()

        self.assertEqual(expected, actual)
