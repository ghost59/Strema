from data import Player, Enemy
from cards import state, munch, tether, shields, shatterd,void, healer

import random
player= Player("james", 100, 10, 10, state)
enemy = Enemy("bob", 100, 10, 10, state)

active_turn = "player"
def draw_card():
    choices = [munch, tether, shields, shatterd, void, healer]
    for cards in player.cards.hand:
        if len(player.cards.hand) <5:
            player.cards.hand.append(random.choice(choices))
        print(cards.name)
def discard():
    choice = input("pick a card to dicard: ")
    if choice in player.cards.hand:
        player.cards.discard_pile.append(choice)
        player.cards.hand.remove(choice)
        print(player.cards.discard_pile)
        print(choice.name)

def show():
    for cards in player.cards.hand:
        print(cards.name)

def Attack():
    choice = input("Pick your card:")
    choices = {"munch": munch, "tether": tether, "shield": shields, "shattered": shatterd, "void": void}
    player.mana -= choices[choice].mana_cost
    enemy.health -= choices[choice].attack_power
    print(enemy.health, enemy.name, player.mana)

def enemy_turn():
    global active_turn
    choices =  {"munch": munch, "tether": tether, "shield": shields, "shattered": shatterd, "void": void}
    if enemy.mana > 0:
       pick = random.choice(list(choices.keys()))
       enemy.mana -= choices[pick].mana_cost
       player.health -= choices[pick].attack_power
       print(choices[pick].name)
    
    print(player.health, player.name)
    print(enemy.mana)
    active_turn = "player"




def player_turn():
    global active_turn
    if player.mana > 0:
        print("""A:Draw A card
        B:Discard a  card
        C: Attack enemy
        S: Show hand
        H:Heal
        Q:Quit""")
        choice = input("Pick your power: ").lower()

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
            case "p":
                active_turn = "enemy"
    active_turn = "enemy"
                
        
            
def gamestate():
    global active_turn
    while player.health > 0 and enemy.health > 0:
        if active_turn == "player":
            player_turn()
            player.mana += 10
        if active_turn == "enemy":
            enemy_turn()
            enemy.mana += 10
            
gamestate()


            


            

