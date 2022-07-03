import unittest
from src.room import Room
from src.guest import Guest
# from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room A", 8, 0, "Hey Jude")
        self.guest_1 = Guest("Paul", 10, "Hey Jude")

    
    def test_room_has_name(self):
        self.assertEqual("Room A", self.room_1.room_name)
    
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEquals(1, self.room_1.check_capacity())
        
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEquals(0, self.room_1.check_capacity())
  