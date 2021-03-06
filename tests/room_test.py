import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room A", 4, 10)
        self.room_2 = Room("Room B", 2, 5)
        self.room_3 = Room("Room C", 1, 19)
        
        self.guest_1 = Guest("Paul", 15, "Hey Jude")
        self.guest_2 = Guest("John", 5, "Let It Be")
        self.guest_3 = Guest("Ringo", 20, "Help!")
        self.guest_4 = Guest("George", 20, "Come Together")
        
        self.song_1 = Song("Signs", "Snoop Dogg")
        self.song_2 = Song("Technologic", "Daft Punk")
        self.song_3 = Song("Hey Jude", "The Beatles")

    
    def test_room_has_name(self):
        self.assertEqual("Room A", self.room_1.room_name)
        
    def test_room_has_capacity_limit(self):
        self.assertEqual(4, self.room_1.capacity)
    
    def test_room_has_till(self):
        self.assertEqual(0, self.room_1.till)
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room_1.check_capacity())
        
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(0, self.room_1.check_capacity())
        
    def test_room_accepts_multiple_guests_within_capcacity(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.assertGreaterEqual(self.room_1.capacity, self.room_1.check_capacity())
    
    def test_room_rejects_multiple_guests_over_capacity(self):
        self.room_2.add_guest_to_room(self.guest_1)
        self.room_2.add_guest_to_room(self.guest_2)
        self.room_2.add_guest_to_room(self.guest_3)
        self.assertEqual("Room B is at full capacity! The capcity for this room is 2 guest[s].", self.room_2.add_guest_to_room(self.guest_3))
  
    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.assertEqual({self.song_1.name: self.song_1.artist}, self.room_1.playlist)
        
    def test_add_multiple_songs_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.room_1.add_song_to_playlist(self.song_2.name, self.song_2.artist)
        self.assertEqual({self.song_1.name: self.song_1.artist, self.song_2.name: self.song_2.artist}, self.room_1.playlist)
        
    def test_guest_can_afford_higher_fee_added_to_till(self):
        self.room_3.add_guest_to_room(self.guest_4)
        self.guest_4.pay_entrance_fee(self.room_3.fee)
        self.assertEqual(1, self.room_3.check_capacity())
        self.assertEqual(19, self.room_3.till)
        self.assertEqual(1, self.guest_4.wallet)
    
    def test_guest_rejected_can_afford_higher_fee_no_capacity(self):
        self.room_3.add_guest_to_room(self.guest_4)
        self.guest_4.pay_entrance_fee(self.room_3.fee)
        self.room_3.add_guest_to_room(self.guest_3)
        self.guest_3.pay_entrance_fee(self.room_3.fee)
        self.assertEqual(1, self.room_3.check_capacity())
        self.assertEqual(19, self.room_3.till)
        self.assertEqual(1, self.guest_4.wallet)
        self.assertEqual("Room C is at full capacity! The capcity for this room is 1 guest[s].", self.room_3.add_guest_to_room(self.guest_3))
    
    def test_guest_cannot_afford_high_fee(self):
        self.guest_1.pay_entrance_fee(self.room_3.fee)
        self.room_3.add_guest_to_room(self.guest_1)
        self.assertEqual(0, self.room_3.check_capacity())
        self.assertEqual(0, self.room_3.till)
        
    def test_multiple_guests_can_afford_fees_added_to_till_one_guest_rejected(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.add_guest_to_room(self.guest_4)
        self.assertEqual(30, self.room_1.till)
        self.assertEqual(3, self.room_1.check_capacity())
    
    
    def test_guest_favourite_song_in_playlist_true(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.room_1.add_song_to_playlist(self.song_2.name, self.song_2.artist)
        self.room_1.add_song_to_playlist(self.song_3.name, self.song_3.artist)
        self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist)
        self.assertEqual(True, self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist))
    
    def test_guest_favourite_song_in_playlist_false(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_song_to_playlist(self.song_1.name, self.song_1.artist)
        self.room_1.add_song_to_playlist(self.song_2.name, self.song_2.artist)
        self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist)
        self.assertEqual(False, self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist))
    
    def test_react_to_favourite_song_positive(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_song_to_playlist(self.song_3.name, self.song_3.artist)
        self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist)
        self.guest_1.react_to_favourite_song(self.room_1.playlist)
        self.assertEqual("Whooo yeah! This is my jam.", self.guest_1.react_to_favourite_song(self.room_1.playlist))
    
    def test_react_to_favourite_song_negative(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_song_to_playlist(self.song_2.name, self.song_2.artist)
        self.guest_1.check_playlist_for_favourite_song(self.room_1.playlist)
        self.guest_1.react_to_favourite_song(self.room_1.playlist)
        self.assertEqual("No singing for me today", self.guest_1.react_to_favourite_song(self.room_1.playlist))