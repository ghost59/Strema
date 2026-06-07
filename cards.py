from data import Card, CardState




def grow(target_card: Card):
    target_card.attack_power += 12
    return target_card.attack_power
   
def voids(target_card: Card):
    target_card.attack_power += 12
    return target_card.attack_power
    

munch = Card("Munch", 10, "attack", 10, "Munches down on the enemies", "grows after every kill", grow)
tether = Card("Tether", 5, "attack", 5 ,"Tether holds enemies down.", "skips an enemy turn,", grow)
cards = [munch, tether]
state = CardState()
state.hand.append(munch)
state.hand.append(tether)

void = Card("Void", 10, "Attack", 10, "Devours souls", "kills", voids)

munch.effect(munch)

void.effect(void)

enemy_card = CardState()