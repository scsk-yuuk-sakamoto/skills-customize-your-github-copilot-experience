
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in which a player guesses letters to reveal a hidden word. Practice using strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Task 1: Set Up the Game

#### Description
Create the word list and initialize the game by randomly selecting a hidden word and preparing its displayed progress and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display one blank position for each letter in the hidden word, such as `_ _ _`.
- Start with a fixed number of incorrect guesses available and track how many remain.

### 🛠️ Task 2: Play a Round

#### Description
Let the player guess letters until they reveal the word or run out of incorrect guesses.

#### Requirements
Completed program should:

- Accept a letter guess from the player and update the displayed progress when the letter is in the word.
- Reduce the remaining attempts for an incorrect guess.
- End the game when the word is guessed or no attempts remain.
- Display a win message when the player guesses the word and a lose message when attempts run out.
