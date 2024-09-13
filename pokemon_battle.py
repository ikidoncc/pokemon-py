from random import uniform, randrange
from time import sleep
import os

pokemon_names = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
    "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
    "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill",
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def two_decimal(value):
    return float("%.2f" % value)

def generate_integer(_min, _max, _interval=1):
    return randrange(_min, _max, _interval)

def generate_float(_min, _max):
    _ = uniform(_min, _max)
    return two_decimal(_)

def generate_pokemon(name):
    return Pokemon(
        name=name,
        level=generate_integer(_min=1, _max=55),
        life=generate_integer(_min=1000, _max=3000),
        force=generate_integer(_min=200, _max=500),
        armor_penetration=generate_integer(_min=10, _max=100),
        armor=generate_integer(_min=50, _max=200)
    )

class Pokemon:
    def __init__(self, level, name, life, force, armor_penetration, armor) -> None:
        self.level = level
        self.name = name
        self.life = life + (self.level * 100)
        self.force = force + (self.level * 2)
        self.armor_penetration = armor_penetration + (self.level * 2) 
        self.armor = armor + (self.level * 5)

    def attack(self, enemy):
        bonus = generate_float(_min=1, _max=1.5)
        dodge = generate_integer(_min=0, _max=10)
        
        pre_remaining_enemy_armor = two_decimal(enemy.armor - self.armor_penetration)
        remaining_enemy_armor = pre_remaining_enemy_armor if pre_remaining_enemy_armor > 0 else 0

        pre_damage = two_decimal(self.force * bonus - remaining_enemy_armor)
        damage = pre_damage if pre_damage > 0 else 0

        print(f"{self.name}: attacks with {damage} damage.")

        if dodge <= 2:
            print(f"> {enemy.name} dodged the attack.")
            return
        
        enemy.life = two_decimal(enemy.life - damage)

        if enemy.life < 0:
            enemy.life = 0

    def defeat(self):
        return self.life <= 0

def current_status_pokemon(pokemon):
    status_pokemon = vars(pokemon)
    status_log = "\n".join(f"{attribute.capitalize()}: {status_pokemon[attribute]}" for attribute in status_pokemon)
    print(status_log)

def play_game():
    clear_terminal()
    print("Welcome to Pokemon")

    while True:
        clear_terminal()
        print("\nPokemons: ")
        
        for pokemon in pokemon_names:
            print(f"{pokemon_names.index(pokemon)} - {pokemon}")
    
        try:
            _ = int(input("\nSelect your pokemon: "))
            
            if 0 <= _ < len(pokemon_names):
                player1_pokemon = pokemon_names[_]
                break
            else:
                print("Warning: Only the listed Pokémon can be selected.")
                sleep(2)
        except:
            print("Error: Please select the pokemon based on the numbers only.")
            sleep(2)

    clear_terminal()
    print(f"!!! Player 1 selected {player1_pokemon} pokemon !!!")

    player1 = generate_pokemon(player1_pokemon)
    
    _ = generate_integer(_min=0, _max=len(pokemon_names) - 1)
    player2_pokemon = pokemon_names[_]

    print(f"!!! Player 2 selected {player2_pokemon} pokemon !!!")

    player2 = generate_pokemon(player2_pokemon)

    sleep(2)

    for time in reversed(range(5)):
        clear_terminal()
        print(f"Battle starts in {time + 1}")
        sleep(1)
        
    presentation = True
    round_count = 1
    
    while True:
        clear_terminal()

        if presentation:
            presentation = False
            print("\n------Presentation------")
            current_status_pokemon(player1)
            print()
            current_status_pokemon(player2)
            sleep(5)
            continue

        print(f"\n----- Round {round_count} -----")

        if player1.defeat():
            print("\n------Status------")
            current_status_pokemon(player1)
            print()
            current_status_pokemon(player2)

            print(f"\n{player2.name} won!\nYou are defeated.")
            break

        if player2.defeat():
            print("\n------Status------")
            current_status_pokemon(player1)
            print()
            current_status_pokemon(player2)

            print(f"\n{player1.name} won!\nYou win!")
            break
        
        print("\n------Attacks-----")
        if not player1.defeat():
            player1.attack(player2)
        if not player2.defeat():
            player2.attack(player1)

        print("\n------Status------")
        current_status_pokemon(player1)
        print()
        current_status_pokemon(player2)

        round_count += 1
        sleep(5)

def main():
    while True:
        play_game()
        print("\nDo you want to play again? Press Enter to play again or type 'exit' to quit.")
        user_input = input().strip().lower()
        if user_input == 'exit':
            break

if __name__ == "__main__":
    main()
