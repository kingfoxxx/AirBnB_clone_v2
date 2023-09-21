#!/usr/bin/python3
"""tests basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """tests review """

    def __init__(self, *args, **kwargs):
        """tests constructor """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """tests place id """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)


    def test_user_id(self):
        """test user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """testa value"""
        new = self.value()
        self.assertNotEqual(type(new.text), str)
