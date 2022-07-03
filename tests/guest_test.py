import unittest
from src.guest import Guest
# from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Paul", 10, "Hey Jude")
    
    def test_guest_has_name(self):
        self.assertEqual("Paul", self.guest.name)
        
    def test_guest_has_money_in_wallet(self):
        self.assertIsNot(0 and None, self.guest.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertIsNot(None, self.guest.favourite_song)