# Pokémon Battle Game - Python Project


## Overview
This is a simple, text-based Pokémon battle simulation game developed in Python. The game allows you to select a Pokémon, battle against another randomly selected Pokémon, and experience a turn-based battle system. Each Pokémon has unique attributes like level, life, force, armor penetration, and armor, which influence the outcome of the battle.

The game can be run on Windows and Linux using the pre-built executables provided in the ./dist folder.

## Features
- Turn-based battle between two Pokémon
- Random opponent selection from a list of 15 Pokémon
- Dynamic attribute generation (level, life, force, armor, etc.)
- Dodging mechanism for more realistic battles
- Detailed round-by-round status updates
- Option to replay the game

## How to Run
### Using Pre-built Executables:
- Windows: Run the .exe file located in the ./dist folder.
- Linux: Run the executable for Linux located in the ./dist folder.

### Running from Source:
1. Ensure Python is installed on your system (version 3.6+ recommended).
2. Clone or download the repository.
3. Open a terminal and navigate to the project directory.
4. Run the following command to start the game:
```bash
python main.py
```

## Game Flow
1. Select your Pokémon: From the list of available Pokémon, choose one to represent you.
2. Random opponent: The game will randomly select another Pokémon to battle against you.
3. Battle Start: The game provides a countdown before starting the battle.
4. Rounds: Each Pokémon takes turns attacking, and damage is calculated based on their stats.
5. Victory or Defeat: The battle continues until one Pokémon's life reaches zero.

## Pokémon Attributes
Each Pokémon is generated with the following stats:

- Level: Randomly generated between 1 and 55, affecting all other stats.
- Life: Randomly generated between 1000 and 3000, increased based on level.
- Force: Randomly generated between 200 and 500, increased based on level.
- Armor Penetration: Determines how much armor the Pokémon can ignore during attacks.
- Armor: Determines how much damage is absorbed when attacked.

## Key Functions
- generate_pokemon(name): Creates a Pokémon with random stats based on the provided name.
- attack(): Executes an attack on the enemy Pokémon, considering dodge chances and armor penetration.
- defeat(): Checks if the Pokémon’s life has dropped to zero or below.
- current_status_pokemon(pokemon): Displays the current stats of the given Pokémon.

## Sample Gameplay

1. Pokémon Selection:
- User selects a Pokémon (e.g., Charmander).
- The game randomly selects another Pokémon (e.g., Squirtle).

2. Battle Simulation:
- Both Pokémon take turns attacking each other.
- The battle status is printed after each round, showing remaining life and other stats.

3. Victory/Defeat:

- The game continues until one Pokémon's life is reduced to zero. The winner is announced, and the option to play again is provided.

## Future Enhancements
- Adding more Pokémon.
- Introducing abilities or special attacks for each Pokémon.
- Implementing a player vs. player mode.

## Credits
Developed by **ikidoncc**. Inspired by the Pokémon battle mechanics.

---

Enjoy your Pokémon battles!
