class Room:

    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
        self.till = 0.00
        self.guest_list = []
        self.playlist = []

    def hire_out_room(self, room, guest):
        if guest.wallet > self.fee:
            if len(self.guest_list) < 1:
                guest.pay(guest, room.fee)
                self.till += room.fee
                self.guest_list.append(guest.name)
            
            

    #need to add if room is full, say no

