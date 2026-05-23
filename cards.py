from data import Card, Cards, Deck

class Tether(Card):
    def __init__(self):
        pass
    def card_types(self):
        self.card_type = "Attacker"
    def decrip(self):
        self.description = "Jagged chains strip your enemies souls"
    def cost(self):
        self.mana_cost -= 5
        return self.mana_cost
    def attack_powers(self):
        self.attack_power = 10
        return self.attack_power