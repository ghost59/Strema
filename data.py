import random
from dataclasses import dataclass
import sdl3
from cards import Tether


class Enemy: 
    def __init__(self, attack, health, attack_power):
        self.attack = attack
        self.health = health
        self.attack_power = attack_power
        
        self.mana = 10
    def health_status(self):
        return self.health
    def Attacks(self):
        num = random.randint(1, 3)
        fire = 100
        life = 200
        evil = 30
        picks = [fire,life,evil]

        random.shuffle(picks)
        chosen = random.choice(picks)
        if chosen == fire:
            self.mana -= 5
        elif chosen == life:
            self.mana -= 10
        elif chosen == evil:
            self.mana -= 10

        return chosen


        
   

class Player:
    def __init__(self, attack: int, health: int, attack_power: int,):
        self.attack = attack
        self.health = health
        self.attack_power = attack_power
        
        self.mana = 10
        self.defense = 5
    def health_status(self):
        return self.health
    def Attacks(self, pows):

    
        teth = Tether()
        butt = 300
        yesss = 20000
        if pows == "tether":
            self.mana -= teth.mana_cost
            results = teth.attack_powers()
        if pows == "butt":
            self.mana -= 7
            results = butt
        if pows == "yesss":
            self.mana -= 10
            results = yesss
        return results
    def Defense(self):
        choice = input("pick you power")
        shield = 10
        life = 15
        if choice == shield:
            self.mana -= 5
            self.defense += shield
        elif choice == life:
            self.mana -= 10
            self.defense += life
        return self.defense

@dataclass()
class Card:
    name: str
    mana_cost: int
    card_type:str
    x: int
    y: int
    h: int
    w: int 
    attack_power: int
    description: str
    effect: str

@dataclass()
class Cards:
    cards: list
    

@dataclass()
class Deck:
    deck: Cards
    hand: int


    

class card_form(Card):
    def form(self):
        rect = sdl3.SDL_FRect(self.x, self.y, self.h, self.w)
        return rect
    



