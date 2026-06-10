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
    choice = input("pick a card to dicard: ")
    for card in player.cards.hand:
         if choice == choice:
             player.cards.discard_pile.append(card)
             player.cards.hand.remove(card)
             print(player.cards.discard_pile)
             print(card.name)

def show():
    for cards in player.cards.hand:
        print(cards.name)

def Attack():
    choice = input("Pick your card:")
    for choice in player.cards.hand:
        enemy.health -= choice.effect(choice)
        player.mana -= choice.mana_cost
        if choice == player.cards.hand:
            print(choice.name)
    print(enemy.health, enemy.name, player.mana)

def enemy_turn():
    
    while enemy.mana > 0:
        for card in enemy.cards.hand: 
            player.health -= card.attack_power


def player_turn():
    
    
    while player.mana > 0:
        print("A:Draw A card, \n" \
        "B:Discard a  card\n" \
        "C: Attack enemy\n" \
        "S: Show hand\n" \
        "H:Heal")
        choice = input("Pick your power: ")

        match choice:
            case "a":
                draw_card()
            case "b":
                discard()
            case "c":
                Attack()
            case "s":
                show()
            case "h":
                healer.effect(healer, player)
            case "q":
                break
        
            
player_turn()

            




            


            

