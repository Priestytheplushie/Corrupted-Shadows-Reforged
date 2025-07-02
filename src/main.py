import tkinter as tk

# Import your main game class from src/game/game.py
from game.game import CorruptedShadows

# --- Main Application Execution ---
if __name__ == "__main__":
    game = CorruptedShadows()

    # Run the main game loop.
    game.run()