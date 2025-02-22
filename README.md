# BirdKiller

## Description
BirdKiller is a simple Pygame-based shooting game where the player controls a shooter to hit birds while avoiding eggs. The player earns points by hitting birds with bullets. If the player is hit by an egg, the game ends. The objective is to score as many points as possible before the game ends.

## Features
- **Player Movement:** The player can move the shooter left and right across the screen.
- **Shooting Mechanism:** The player can shoot bullets at the birds, with a limit on the number of bullets on the screen at any given time.
- **Bird Movement:** Birds move across the screen, changing direction when they hit the screen edges.
- **Egg Dropping:** Birds randomly drop eggs, and if the player is hit by an egg, the game ends.
- **Score System:** The player earns points by shooting birds, and the score is displayed on the screen.
- **Game Over:** The game ends when the player is hit by an egg, and a "Game Over" message appears.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/BirdKiller.git
   ```

2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python bird_killer.py
   ```

## Controls
- **Left Arrow:** Move the shooter left.
- **Right Arrow:** Move the shooter right.
- **Space Bar:** Shoot bullets at the birds.

## Dependencies
- `pygame`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
