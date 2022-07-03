import unittest
from src.guest import Guest
from src.room import Room

# from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Paul", 15, "Hey Jude")
        self.guest_2 = Guest("John", 5, "Let It Be")
        
        self.room_1 = Room("Room A", 4, 10)
    
    def test_guest_has_name(self):
        self.assertEqual("Paul", self.guest_1.name)
    
    def test_guest_has_favourite_song(self):
        self.assertIsNot(None, self.guest_1.favourite_song)
        
    def test_guest_has_some_money_in_wallet(self):
        self.assertIsNot(0 and None, self.guest_1.wallet)
    
    def test_can_afford_fee_true(self):
        self.assertEqual(True, self.guest_1.can_afford_fee(self.room_1.fee))
        
    def test_can_afford_fee_false(self):
        self.assertEqual(False, self.guest_2.can_afford_fee(self.room_1.fee))
    
    def test_entrance_fee_deducted_from_wallet(self):
        self.guest_1.pay_entrance_fee(self.room_1.fee)
        self.assertEqual(5, self.guest_1.wallet)
    
    