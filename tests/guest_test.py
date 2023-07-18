import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Sean", 30)

    def test_guest_name(self):
        self.assertEqual("Sean", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(30, self.guest.money)