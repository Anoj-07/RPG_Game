from player import Player
from enemie import generate_random_ememy


def battle(player, enemy):
    print(f"\nA wild {enemy._name} appears!")

    while player.is_alive() and enemy.is_alive():
        print("\n ---- Battle status ----")
        print(player.get_status())
        print(enemy.get_status())

        input("\n Press Enter to attack---")
        player.attack(enemy)

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print(f"\n You defeated the {enemy._name}!")
        player.gain_xp(30)
    else:
        print("\n You have been defeated ... Game Over.")

def main():
    print("Welcome to the Rext RPG !")
    player_name = input("Enter Your Name : ")
    player = Player(player_name)

    while player.is_alive():
        enemy = generate_random_ememy()
        battle(player, enemy)

        if not player.is_alive:
            break

        cont = input("\n Do you want to fight another enemy? (y/n) :")
        if cont.lower() != 'y':
            break

    
    print(f"Thanks for playing {player_name}!")

    print(f"Welcome, {player_name}!")
    print(player.get_status)

if __name__ == "__main__":
    main()