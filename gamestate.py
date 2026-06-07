from data import Player, Enemy
from cards import state, munch, tether

import random
player= Player("james", 100, 10, 10, state)
enemy = Enemy("bob", 100, 10, 10, state)
def draw_card():
    choices = [munch, tether]
    for card in player.cards.hand:
        if len(player.cards.hand) <= 2:
            player.cards.hand.append(random.choice(choices))
        print(card.description)
def discard():
    for card in player.cards.hand:
         if card == player.cards.hand:
             player.cards.discard_pile.append(card)
             player.cards.hand.remove(card)
             print(player.cards.discard_pile)
             print(card.name)
def Attack():
    choice = input("Pick your card:")
    for card in player.cards.hand:

        if card == choice:
            enemy.health -= card.attack_power
            player.mana -= card.mana_cost
            print(enemy.health)

    

def player_turn():
    
    
    while player.health > 0 and enemy.health > 0:
        print("A:Draw A card," \
        "B:Discard a  card" \
        "C: Attack enemy")
        choice = input("Pick your power: ")

        match choice:
            case "a":
                draw_card()
            case "b":
                discard()
            case "c":
                Attack()
            case "q":
                break
            
player_turn()

            




            


            

