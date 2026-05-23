from data import Player, Enemy
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
