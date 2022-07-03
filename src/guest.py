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
    
    # def check_wallet_amount(self):
    #     return self.wallet