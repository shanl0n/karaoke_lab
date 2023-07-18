import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.sean = Guest("Sean", 30)
        self.room = Room("The Amber Room")

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.sean)
        self.assertEqual(1, self.room.number_of_guests())

    def test_room_has_name(self):
        self.assertEqual("The Amber Room", self.room.name)

