import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Tom Petty", "Wont Back Down")

def test_song_has_title(self):
        self.assertEqual("Wont Back Down", self.song.title)