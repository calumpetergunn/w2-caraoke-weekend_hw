class Guest:

    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song

    def pay(self, guest, amount):
        self.wallet -= amount