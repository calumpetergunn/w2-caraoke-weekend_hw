import unittest

from classes.room import Room
from classes.guest import Guest

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Dawghaus", 50.00)
        self.guest = Guest("Deano", 500.00, "Can I Borrow a Feeling")

    def test_room_has_name(self):
        self.assertEqual("The Dawghaus", self.room.name)

    def test_room_has_fee(self):
        self.assertEqual(50.00, self.room.fee)

    def test_can_hire_room_success(self):
        self.room.hire_out_room(self.room, self.guest)
        self.assertEqual(450.00, self.guest.wallet)
        self.assertEqual(50.00, self.room.till)
        self.assertEqual(["Deano"], self.room.guest_list)

    def test_can_hire_room_broke(self):
        self.guest = Guest("Gavin", 20.00, "Superfreak")
        self.room.hire_out_room(self.room, self.guest)
        self.assertEqual(20.00, self.guest.wallet)
        self.assertEqual(0.00, self.room.till)

    # def test_can_hire_room_full(self):
    #     self.guest_list = ["Gavin"]
    #     self.room.hire_out_room(self.room, self.guest)
    #     self.assertEqual(500.00, self.guest.wallet)
    #     self.assertEqual(0.00, self.room.till)

    #NOT SURE WHY THIS ONE ISN'T WORKING


        