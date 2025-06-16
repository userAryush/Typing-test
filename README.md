# Speed Typing Test (Terminal)

A simple terminal-based speed typing test implemented in Python using the `curses` library.

## Features
- Displays a random text line for typing practice (loaded from `text.txt`).
- Real-time typing accuracy with color-coded feedback:
  - **Green** for correct characters.
  - **Red** for incorrect characters.
- Calculates and displays Words Per Minute (WPM) dynamically.
- Supports backspace to correct mistakes.
- Exit anytime by pressing the `Esc` key.

## How to Run

1. Make sure you have Python installed (tested with Python 3.x).
2. Place a `text.txt` file in the same directory with lines of sample text for the test.
3. Run the script from your terminal:

   ```bash
   python speed_typing_test.py
