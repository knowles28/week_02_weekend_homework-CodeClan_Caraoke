class Room:
    def __init__(self, _room_name, _capacity, _till):
        self.room_name = _room_name
        self.capacity = _capacity
        self.playlist = {}
        self.guests = []
        self.room_till = _till
    
    def check_capacity(self):
        return len(self.guests)
    
    def add_guest_to_room(self, guest):
        self.guests.append(guest)
        
    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)
    
    def add_song_to_playlist(self, new_song, artist):
        self.playlist.update({new_song: artist})