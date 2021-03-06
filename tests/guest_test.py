import unittest

from classes.guest import Guest
from classes.room import Room

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Deano", 500.00, "Can I Borrow a Feeling")
        self.room = Room("The Dawghaus", 50.00)

    def test_guest_has_name(self):
        self.assertEqual("Deano", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(500.00, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Can I Borrow a Feeling", self.guest.fave_song)

    def test_guest_can_pay(self):
        self.guest.pay(self.guest.name, self.room.fee)
        self.assertEqual(450.00, self.guest.wallet)


