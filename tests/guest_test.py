import unittest

from classes.guest import Guest
from classes.room import Room
from classes.bar import Bar

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Deano", 500.00, "Can I Borrow a Feeling")
        self.room = Room("The Dawghaus", 50.00, 10)
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

    def test_guest_has_name(self):
        self.assertEqual("Deano", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(500.00, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Can I Borrow a Feeling", self.guest.fave_song)

    def test_guest_can_pay(self):
        self.guest.pay(self.guest.name, self.room.fee)
        self.assertEqual(450.00, self.guest.wallet)

    def test_guest_can_pay_tab(self):
        self.guest.pay_bar_tab(self.guest.name)
        self.assertEqual(400.00, self.guest.wallet)

    # def test_drink_can_be_found_by_name(self):
    #     drink = self.guest.find_drink_by_name("Purple Goanna")
    #     self.assertEqual("Purple Goanna", drink["name"])

    # def test_drink_can_be_sold_to_guest(self):
    #     self.guest.sell_drink_to_guest("Beer", self.guest)
    #     self.assertEqual(2.50, self.guest.bar_tab)



