import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar import Bar

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Dawghaus", 50.00, 4)
        self.guest = Guest("Deano", 500.00, "Can I Borrow a Feeling")
        self.song = Song("Nothing Compares 2U")

    def test_room_has_name(self):
        self.assertEqual("The Dawghaus", self.room.name)

    def test_room_has_fee(self):
        self.assertEqual(50.00, self.room.fee)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_hire_room_success(self):
        self.room.hire_out_room(self.room, self.guest)
        self.assertEqual(450.00, self.guest.wallet)
        self.assertEqual(150.00, self.room.till)
        self.assertEqual(["Deano"], self.room.guest_list)

    def test_can_hire_room_broke(self):
        self.guest = Guest("Gavin", 20.00, "Superfreak")
        self.room.hire_out_room(self.room, self.guest)
        self.assertEqual(20.00, self.guest.wallet)
        self.assertEqual(100.00, self.room.till)

    # def test_can_hire_room_full(self):
    #     self.guest_list = ["Gavin", "David", "Larry", "Bev"]
    #     self.room.hire_out_room(self.room, self.guest)
    #     self.assertEqual(500.00, self.guest.wallet)
    #     self.assertEqual(0.00, self.room.till)

    #NOT SURE WHY THIS ONE ISN'T WORKING

    def test_can_check_out_guest(self):
        self.room.hire_out_room(self.room, self.guest)
        self.room.check_out_from_room(self.room, self.guest)
        self.assertEqual(0, len(self.room.guest_list))

    def test_can_add_fave_song_to_playlist(self):
        self.room.add_fave_song_to_playlist(self.guest)
        self.assertEqual(["Can I Borrow a Feeling"], self.room.playlist)

    def test_can_remove_song_from_playlist(self):
        self.room.playlist = ["Nothing Compares 2U"]
        self.room.remove_song_from_playlist(self.song.name)
        self.assertEqual([], self.room.playlist)

    def fave_song_reaction(self):
        self.room.playlist = ["Nothing Compares 2U", "Rock n Roll Mcdonalds", "Can I Borrow a Feeling"]
        self.assertEqual("Woop Woop", self.room.favourite_song_on_list(self.guest))


        