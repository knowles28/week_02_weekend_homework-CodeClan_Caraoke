import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room A", 4)
        self.room_2 = Room("Room B", 2)
        
        self.guest_1 = Guest("Paul", 10, "Hey Jude")
        self.guest_2 = Guest("John", 5, "Let It Be")
        self.guest_3 = Guest("Ringo", 20, "Help!")
        
        self.song_1 = Song("Signs", "Snoop Dogg")
        self.song_2 = Song("One More Time", "Daft Punk")

    
    def test_room_has_name(self):
        self.assertEqual("Room A", self.room_1.room_name)
        
    def test_room_has_capacity_limit(self):
        self.assertEqual(4, self.room_1.capacity)
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room_1.check_capacity())
        
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(0, self.room_1.check_capacity())
        
    def test_room_allows_guests_within_capcacity(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.assertGreaterEqual(self.room_1.capacity, self.room_1.check_capacity())
    
    def test_room_rejects_guests_over_capacity(self):
        self.room_2.add_guest_to_room(self.guest_1)
        self.room_2.add_guest_to_room(self.guest_2)
        self.room_2.add_guest_to_room(self.guest_3)
        self.assertEqual("Room B is at full capacity! The capcity for this room is 2 guests.", self.room_2.add_guest_to_room(self.guest_3))
  
    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.assertEqual({self.song_1.name: self.song_1.artist}, self.room_1.playlist)
        
    def test_add_multiple_songs_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.room_1.add_song_to_playlist(self.song_2.name, self.song_2.artist)
        self.assertEqual({self.song_1.name: self.song_1.artist, self.song_2.name: self.song_2.artist}, self.room_1.playlist)
        
        
