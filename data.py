import random
from dataclasses import dataclass
import sdl3
class GameState:
    def __init__(self, player_turn, enemy_turn):
        self.player_turn = player_turn
        self.enemy_turn = enemy_turn 
        self.player_mana = self.player_turn.mana
        self.enemy_mana = self.enemy_turn.mana
    
    def players_turns(self):
        if self.player_turn.mana  == 0:
            self.enemy_mana = 10 + 1
            self.enemys_turn()
        print("1) Attack,"
        "2)Defence",
        "3)Heal")
        choice = input("enter an choice")
        if choice == "attack":
            attack = self.player_turn.Attack(choice)
            self.enemy_turn.health -= attack
            print(self.enemy_turn.health)
        

    def enemys_turn(self):
        if self.enemy_turn.mana == 0:
            self.player_mana = 10 + 1
            self.players_turns()
        
    def play(self):
        while self.player_turn.health > 0:
            if self.player_mana >= 10:
                self.player_turn.Attacks()
            elif self.enemy_mana >= 10:
                self.enemy_turn.Attacks()

            self.enemys_turn()
            if self.enemy_turn.health == 0:
                print("you have won the war and now you win this war.")
                break


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

    
        fire = 30
        butt = 300
        yesss = 20000
        if pows == "fire":
            self.mana -= 4
            results = fire
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

    description: str
    effect: str

@dataclass()
class Cards:
    cards: list
    

@dataclass()
class Deck:
    deck: Cards
    hand: int
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
    

class card_form(Card):
    def form(self):
        rect = sdl3.SDL_FRect(self.x, self.y, self.h, self.w)
        return rect
    


player = Player(100, 100, 100)
enemy = Enemy(100, 100, 100)

game = GameState(player, enemy)
game.players_turns()

#print(test)

