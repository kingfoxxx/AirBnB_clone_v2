#!/usr/bin/python3
""" Module that tests file state """

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Class that tests the state"""

    def __init__(self, *args, **kwargs):
        """ Constructor for test state class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State



    def test_name3(self):
        """testing of state name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)
