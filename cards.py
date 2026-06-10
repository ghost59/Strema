from data import Card, CardState, Player




def grow(target_card: Card):
    target_card.attack_power += 12
    return target_card.attack_power
   
def voids(target_card: Card):
    target_card.attack_power += 12
    return target_card.attack_power

def shield(target_card: Card):
    target_card.defense += 20
    return target_card.defense

def shatter(target_card: Card):
    for i in range(target_card.attack_power):
        target_card.attack_power +=i 
    return target_card.attack_power
def heal(target_card:Card, player: Player):
    target_card.defense += 10
    player.health += target_card.defense
    print(player.health)
def yeild(target_card: Card):
    target_card.attack_power *= 2
    return target_card.attack_power



    

munch = Card("Munch", 10, "attack", 10, "Munches down on the enemies", "grows after every kill", grow, 10)
tether = Card("Tether", 5, "attack", 5 ,"Tether holds enemies down.", "skips an enemy turn,", grow, 10)
cards = [munch, tether]
state = CardState()
state.hand.append(munch)
state.hand.append(tether)

void = Card("Void", 10, "Attack", 10, "Devours souls", "kills", voids, 10)
shields = Card("Shield", 10, "defense", 10, "Protects them", "keeps the player safe", shield, 10)
shatterd = Card("Shatterd", 4, "attack", 3, "Shatters the enemies mind ", "Enemy loses mind", shatter, 5)
healer = Card("healer", 5, "defense", 0, "heals the player", "health", heal, 0)



munch.effect(munch)

void.effect(void)
shields.effect(shields)
shatterd.effect(shatterd)

enemy_card = CardState()