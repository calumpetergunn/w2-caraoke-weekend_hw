import unittest

from classes.guest import Guest
from classes.room import Room
from classes.bar import Bar

class BarTest(unittest.TestCase):

    def setUp(self):
        self.bar = Bar
        self.guest = Guest("Deano", 500.00, "Can I Borrow a Feeling")
        self.room = Room("The Dawghaus", 50.00, 4)
        self.menu = [
            {"name": "Vodka Coke", 
            "price": 3.50},
            {"name": "Beer", 
            "price": 2.50},
            {"name": "Cement Mixer",
            "price": 2.50},
            {"name": "Purple Goanna",
            "price": 8.50}
        ]
    
    def test_bar_has_till(self):
        self.assertEqual(100, self.room.till)

    def test_bar_has_menu(self):
        self.assertEqual(4, len(self.menu))

