import rich
from rich.progress import track
from rich.console import Console, ConsoleDimensions
from rich import text
from rich import print
from data import Enemy, Player
name = input("Put in you name")
print(f"[blue underline]{name}")

ConsoleDimensions(100, 200)

def main():
    
    player = Player(10, 100, 100, 10)
    
    enemy = Enemy(10, 100, 10, 10)
    quit = True

    while quit == True:
        choice = input("Enter a command: ")
        match choice:
            case "Attack":
                power = input("what power?")
                pw = player.Attacks(power)
                enemy.health -= pw
                print(f"[blue] enemy health {enemy.health}")
            case "Heal":
                player_health += 1
            case "quit":
                quit = False
        if enemy.health <= 0:
            break
        if enemy.health > 0:
            enemy.Attacks()
    

if __name__ == "__main__":
    main()

