# ICT401 Assessment 3 - Individual Programming Project
# Student Name: Julianne Jamie Calma
# Student ID: 202571946
# Core game logic only. This file intentionally has no print() or input().

import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class GameEngine:
    """Manages the state and rules of the word-guessing game."""

    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.secret_word = ""
        self.hint = ""
        self.difficulty = ""
        self.guessed_letters = set()
        self.remaining_lives = max_lives
        self.score = 0

    def load_words(self, filename):
        """Read WORD|Hint records from an external text file."""
        records = []
        file_path = Path(filename)
        if not file_path.is_absolute():
            file_path = BASE_DIR / file_path
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line or "|" not in line:
                        continue
                    word, hint = line.split("|", 1)
                    word = word.strip().upper()
                    hint = hint.strip()
                    if word.isalpha() and hint:
                        records.append((word, hint))
        except (FileNotFoundError, OSError):
            return []
        return records

    def select_word(self, filename, difficulty):
        """Choose a random word from a difficulty file and reset the game."""
        records = self.load_words(filename)
        if not records:
            return False

        self.secret_word, self.hint = random.choice(records)
        self.difficulty = difficulty
        self.guessed_letters = set()
        self.remaining_lives = self.max_lives
        self.score = 0
        return True

    def validate_letter(self, letter):
        """Validate one alphabetic letter and reject duplicate guesses."""
        letter = letter.strip().upper()
        if len(letter) != 1:
            return False, "Please enter only one letter."
        if not letter.isalpha():
            return False, "Invalid input. Please enter a letter, not a number or symbol."
        if letter in self.guessed_letters:
            return False, "You already guessed that letter."
        return True, letter

    def guess_letter(self, letter):
        """Apply a valid guess and return whether it was correct."""
        valid, result = self.validate_letter(letter)
        if not valid:
            return False, result

        letter = result
        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            self.score += self.secret_word.count(letter) * 10
            return True, "Correct guess!"

        self.remaining_lives -= 1
        return True, "Wrong guess!"

    def hidden_word(self):
        """Return the word with unguessed letters shown as underscores."""
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.secret_word
        )

    def has_won(self):
        return bool(self.secret_word) and all(
            letter in self.guessed_letters for letter in set(self.secret_word)
        )

    def has_lost(self):
        return self.remaining_lives <= 0 and not self.has_won()

    def is_over(self):
        return self.has_won() or self.has_lost()

    def save_history(self, interface):
        """Append one completed session to game_history.txt."""
        result = "WIN" if self.has_won() else "LOSS"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        guessed = "".join(sorted(self.guessed_letters))
        line = (
            f"{timestamp}|{interface}|{self.difficulty}|{self.secret_word}|"
            f"{result}|Score:{self.score}|Lives:{self.remaining_lives}|Guesses:{guessed}\n"
        )
        try:
            history_path = BASE_DIR / "game_history.txt"
            with open(history_path, "a", encoding="utf-8") as file:
                file.write(line)
            return True
        except OSError:
            return False
