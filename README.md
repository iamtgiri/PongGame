
# Pong Game

Welcome to the **Pong Game**, a modern recreation of the classic arcade game. This project, developed using Python and Pygame, marks its first release, offering engaging gameplay and dynamic mechanics.

## Features

### Core Gameplay
- **Dynamic Ball Movement**: Ball speed increases with every paddle collision.
- **Angle Variations**: Ball trajectory changes slightly after each paddle hit.
- **Difficulty Levels**: Choose between Easy, Medium, and Hard modes.
- **High Score Tracking**: Automatically saves the highest score locally.

### Visual and Sound Enhancements
- **Minimalist Design**: Clean interface for a focused gaming experience.
- **Score Display**: Real-time and high scores displayed on-screen.
- **Sound Effects**: Includes sounds for ball collisions and scoring.
- **Pause Functionality**: Pause and resume the game with a simple key press.

### Intelligent Opponent
- **Adaptive AI**: The opponent’s paddle behavior adjusts based on the selected difficulty.

## Installation

### Prerequisites
- Python 3.6 or higher
- Pygame 2.0 or higher

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/iamtgiri/pong_game.git
   cd pong_game
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python pong_game.py
   ```

## How to Play

### Controls
- **Arrow Up**: Move paddle up.
- **Arrow Down**: Move paddle down.
- **P**: Pause/Resume the game.

### Game Modes
- At the start menu, select difficulty:
  - **1**: Easy
  - **2**: Medium
  - **3**: Hard

### Objective
Score by bouncing the ball past your opponent while defending your side.

## Project Structure

```
pong_game/
│
├── pong_game.py         # Main game script
├── bounce.wav           # Sound for ball collision
├── score.wav            # Sound for scoring
├── highscore.txt        # File for storing high score
├── README.md            # Project documentation
```

## Future Plans
- Add local multiplayer mode.
- Introduce power-ups for varied gameplay.
- Implement global leaderboards.

## Feedback and Contributions
This is the first release of **Pong Game**. Your feedback and suggestions are highly welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
