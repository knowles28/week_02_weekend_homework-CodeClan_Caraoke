class Room:
    def __init__(self, _room_name, _capacity):
        self.room_name = _room_name
        self.capacity = _capacity
        self.playlist = {}
        self.guests = []
        self.room_till = 0
    
    def check_capacity(self):
        return len(self.guests)
    
    def add_guest_to_room(self, guest):
        if self.check_capacity() < self.capacity:
            self.guests.append(guest)
        else:
            return f"{self.room_name} is at full capacity! The capcity for this room is {self.capacity} guests."

        
    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)
    
    def add_song_to_playlist(self, new_song, artist):
        self.playlist.update({new_song: artist})