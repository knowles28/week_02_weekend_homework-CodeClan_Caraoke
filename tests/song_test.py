import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Wonderwall", "Oasis")
        
    def test_song_has_name(self):
        self.assertEqual("Wonderwall", self.song.name)
        
    def test_song_has_artist(self):
        self.assertEqual("Oasis", self.song.artist)