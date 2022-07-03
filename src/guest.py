import re


class Guest:
    def __init__(self, _name, _wallet, _favourite_song):
        self.name = _name
        self.wallet = _wallet
        self.favourite_song = _favourite_song
    
    def pay_entrance_fee(self, fee):
        if self.can_afford_fee(fee):
            self.wallet -= fee
    
    def can_afford_fee(self, fee):
        return self.wallet >= fee
    

    
    def check_playlist_for_favourite_song(self, playlist):
        for song in playlist:
            if song == self.favourite_song:
                return True
        else:
            return False
    # PROBLEMS WITH THE ELSE PART OF THIS LOOP WHEN SETTING UP
    
    def react_to_favourite_song(self, playlist):
        if self.check_playlist_for_favourite_song(playlist):
            return "Whooo yeah! This is my jam."
        else:
            return "No singing for me today"
        
    

# def old_check_playlist_for_favourite_song(self, playlist):
#         for song in playlist.keys(): ????
#             if song == self.favourite_song:
#                 return "Whooo yeah! This is my jam."
#             else:
#                 return "No singing for me today"
        