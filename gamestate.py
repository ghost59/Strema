from data import Player, Enemy
from cards import state, munch, tether, shields, shatterd,void, healer

import random
player= Player("james", 100, 10, 10, state)
enemy = Enemy("bob", 100, 10, 10, state)
def draw_card():
    choices = [munch, tether, shields, shatterd, void, healer]
    for card in player.cards.hand:
        if len(player.cards.hand) <5:
            player.cards.hand.append(random.choice(choices))
        print(card.description)
def discard():
    choice = input("pick a card to dicard")
    for choice in player.cards.hand:
         if choice == player.cards.hand:
             player.cards.discard_pile.append(choice)
             player.cards.hand.remove(choice)
             print(player.cards.discard_pile)
             print(choice.name)
def Attack():
    choice = input("Pick your card:")
    for choice in player.cards.hand:
        enemy.health -= choice.effect(choice)
        player.mana -= choice.mana_cost
        if choice == player.cards.hand:
            print(choice.name)
    print(enemy.health, enemy.name, player.mana)

    

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

            




            


            

