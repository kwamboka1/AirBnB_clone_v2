#!/usr/bin/python3

""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests amenity """

    def __init__(self, *args, **kwargs):
        
        """ Tests to check all arguments are working"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        
        """ tests for secnd name """
        new = self.value()
        self.assertEqual(type(new.name), str)
