import unittest

from classes.song import Song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Nothing Compares 2U")

    def test_song_has_name(self):
        self.assertEqual("Nothing Compares 2U", self.song.name)