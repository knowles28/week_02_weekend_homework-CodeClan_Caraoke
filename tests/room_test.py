import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room A", 8, 0)
        self.guest_1 = Guest("Paul", 10, "In Da Club")
        self.song_1 = Song("Signs", "Snoop Dogg")

    
    def test_room_has_name(self):
        self.assertEqual("Room A", self.room_1.room_name)
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room_1.check_capacity())
        
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(0, self.room_1.check_capacity())
  
    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.assertEqual({self.song_1.name: self.song_1.artist}, self.room_1.playlist)