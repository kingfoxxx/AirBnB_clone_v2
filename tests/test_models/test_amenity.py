#!/usr/bin/python3
"""test for amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """this will test amenity class"""

    def __init__(self, *args, **kwargs):
        """it tests argument"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity


    def test_name2(self):
        """it tests name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
