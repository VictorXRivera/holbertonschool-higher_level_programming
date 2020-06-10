#!/usr/bin/python3
""" Unit test for base """


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Tests for id """
    def test_base(self):
        test_b1 = Base()
        self.assertEqual(test_b1.id, 1)
        test_b2 = Base()
        self.assertEqual(test_b2.id, 2)
        test_b3 = Base()
        self.assertEqual(test_b3.id, 12)
