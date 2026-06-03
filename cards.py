from data import Card




def grow():
    munch.attack_power += 12


munch = Card("Munch", 10, "attack", 10, "Munches down on the enemies", "grows after every kill", grow)
