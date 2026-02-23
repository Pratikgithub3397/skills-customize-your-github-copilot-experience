# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the foundation of the Hangman game by implementing word selection and game initialization.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Initialize the game with a hidden word display (e.g., `_ _ _ _ _`)
- Track total incorrect guesses allowed (default 6)
- Display the initial game state to the player


### 🛠️ Implement Guessing Mechanism

#### Description
Add functionality for players to guess letters and update the game state based on their guesses.

#### Requirements
Completed program should:

- Accept letter guesses from the player using `input()`
- Check if the guessed letter is in the word
- Update the hidden word display with correctly guessed letters
- Track incorrect guesses and remaining attempts
- Prevent duplicate guesses and inform the player


### 🛠️ Game Logic and Win/Lose Conditions

#### Description
Implement the core game loop and end-game logic to determine win/lose states.

#### Requirements
Completed program should:

- Continue the game loop until the word is fully revealed or attempts are exhausted
- Display win message when the word is guessed correctly
- Display lose message when attempts run out, revealing the word
- Show final game statistics (guesses made, word revealed, etc.)
