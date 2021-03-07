class Room:

    def __init__(self, name, fee, capacity):
        self.name = name
        self.fee = fee
        self.till = 100.00
        self.capacity = capacity
        self.guest_list = []
        self.playlist = []

    def hire_out_room(self, room, guest):
        if guest.wallet > self.fee:
            if len(self.guest_list) < self.capacity:
                guest.pay(guest, room.fee)
                self.till += room.fee
                self.guest_list.append(guest.name)

    def check_out_from_room(self, room, guest):
        self.guest_list.remove(guest.name)

    def add_fave_song_to_playlist(self, guest):
        self.playlist.append(guest.fave_song)

    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)

    def favourite_song_on_list(self, guest):
        for song in self.playlist:
            if song == guest.fave_song:
                return "Woop Woop"
            return


    #favourite song
    # bar tab, add to
    # pay bar tab
            

    #need to add if room is full, say no

