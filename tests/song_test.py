import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Wonderwall_Oasis")
        
    def test_song_has_name(self):
        self.assertEqual("Wonderwall_Oasis", self.song.name)