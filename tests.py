import random
def taco():
    tacos = ["Tacos", "aco", "yes"]
    pick = random.choice(tacos)
    return pick
test = taco()
print(test)