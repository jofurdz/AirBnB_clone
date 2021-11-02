#!/usr/bin/python3
"""Amenity class test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing of the Amenity Class"""

    def setUp(self):
        '''Turn Amenity into Amenity variable'''

        self.amenity = Amenity()
        pass

    def tearDown(self):
        """tear down after methods"""
        pass

        self.assertEqual(self.amenity.name, "")

        Dic = self.amenity.to_dict()
        ob = Amenity(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.amenity is ob)


    if __name__ == '__main__':
        unittest.main()
