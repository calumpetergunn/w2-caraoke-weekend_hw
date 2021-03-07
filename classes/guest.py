class Guest:

    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song
        self.bar_tab = 0
        self.menu = [
            {"name": "Vodka Coke", 
            "price": 3.50},
            {"name": "Beer", 
            "price": 2.50},
            {"name": "Cement Mixer",
            "price": 2.50},
            {"name": "Purple Goanna",
            "price": 8.50}
        ]

    def pay(self, guest, amount):
        self.wallet -= amount

    def pay_bar_tab(self, guest):
        self.bar_tab = 100
        self.wallet -= self.bar_tab

    def find_drink_by_name(self, drink_name):
        correct_drink = None

        for drink in self.menu:
            if drink_name == drink["name"]:
                drink = correct_drink
        
        return correct_drink

    # def sell_drink_to_guest(self, drink_name, guest):
    #     for drink in self.menu:
    #         if drink_name == drink["name"]:
    #             self.wallet += drink["price"]

    # self.guest.menu[3]["price"]

    

    

