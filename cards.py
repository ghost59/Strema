from data import Card, Cards, Deck, Enemy 

class Tether(Card):
    def __init__(self):
        pass
    def card_types(self):
        self.card_type = "Attacker"
    def decrip(self):
        self.description = "Jagged chains strip your enemies souls"
    def cost(self):
        self.mana_cost = 5
        return self.mana_cost
    def attack_powers(self):
        self.attack_power = 10
        return self.attack_power
class Munch(Card):
    def __init__(self):
        self.size = 0

    def card_types(self):
        self.card_type = "Attacker"
    def descrip(self):
        self.description = "Munch, bite down on your enemies with the power of a god"
    def cost(self):
        self.mana_cost = 6
        return self.mana_cost
    def attack_powers(self):
        self.attack_power = 12
        return self.attack_power
    def increae(self):
        self.size += 10
        

    