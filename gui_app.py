# ICT401 Assessment 3 - Individual Programming Project
# Student Name: Julianne Jamie Calma
# Student ID: 202571946
# Graphical User Interface (GUI) using tkinter only.

import tkinter as tk
from tkinter import messagebox
from engine import GameEngine


class WordGuessingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ICT401 Word Guessing Game")
        self.root.geometry("760x600")
        self.root.resizable(False, False)

        self.engine = GameEngine(max_lives=6)
        self.letter_buttons = {}

        title = tk.Label(root, text="WORD GUESSING GAME", font=("Arial", 22, "bold"))
        title.pack(pady=(18, 8))

        difficulty_frame = tk.Frame(root)
        difficulty_frame.pack(pady=5)
        tk.Label(difficulty_frame, text="Difficulty:", font=("Arial", 11, "bold")).pack(side="left")
        self.difficulty_var = tk.StringVar(value="Easy")
        for level in ("Easy", "Medium", "Hard"):
            tk.Radiobutton(
                difficulty_frame,
                text=level,
                variable=self.difficulty_var,
                value=level,
            ).pack(side="left", padx=6)
        tk.Button(difficulty_frame, text="New Game", command=self.start_game).pack(side="left", padx=15)

        self.hint_label = tk.Label(root, text="Hint: -", font=("Arial", 12), wraplength=680)
        self.hint_label.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Courier New", 28, "bold"))
        self.word_label.pack(pady=15)

        status_frame = tk.Frame(root)
        status_frame.pack(pady=5)
        self.lives_label = tk.Label(status_frame, text="Lives: 6", font=("Arial", 12, "bold"))
        self.lives_label.pack(side="left", padx=25)
        self.score_label = tk.Label(status_frame, text="Score: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(side="left", padx=25)

        self.message_label = tk.Label(root, text="Choose letters below.", font=("Arial", 12))
        self.message_label.pack(pady=10)

        keyboard_frame = tk.Frame(root)
        keyboard_frame.pack(pady=10)

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for index, letter in enumerate(letters):
            row = index // 9
            column = index % 9
            button = tk.Button(
                keyboard_frame,
                text=letter,
                width=5,
                height=2,
                command=lambda value=letter: self.make_guess(value),
            )
            button.grid(row=row, column=column, padx=3, pady=3)
            self.letter_buttons[letter] = button

        self.start_game()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        filename = difficulty.lower() + ".txt"

        if not self.engine.select_word(filename, difficulty):
            messagebox.showerror(
                "File Error",
                f"'{filename}' is missing, broken, or has no valid WORD|Hint records.",
            )
            self.set_keyboard_state("disabled")
            return

        for button in self.letter_buttons.values():
            button.config(state="normal")

        self.message_label.config(text="Choose a letter.")
        self.refresh_display()

    def make_guess(self, letter):
        # Buttons send letters only, but the GameEngine still performs validation.
        valid, message = self.engine.guess_letter(letter)
        if not valid:
            self.message_label.config(text=message)
            return

        self.letter_buttons[letter].config(state="disabled")
        self.message_label.config(text=message)
        self.refresh_display()

        if self.engine.is_over():
            self.finish_game()

    def refresh_display(self):
        self.hint_label.config(text=f"Hint: {self.engine.hint}")
        self.word_label.config(text=self.engine.hidden_word())
        self.lives_label.config(text=f"Lives: {self.engine.remaining_lives}")
        self.score_label.config(text=f"Score: {self.engine.score}")

    def set_keyboard_state(self, state):
        for button in self.letter_buttons.values():
            button.config(state=state)

    def finish_game(self):
        self.set_keyboard_state("disabled")
        self.refresh_display()
        self.engine.save_history("GUI")

        if self.engine.has_won():
            result = f"You won! The word was {self.engine.secret_word}."
        else:
            result = f"You lost. The word was {self.engine.secret_word}."

        self.message_label.config(text=result)
        messagebox.showinfo("Game Over", f"{result}\nScore: {self.engine.score}")


def main():
    root = tk.Tk()
    WordGuessingGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
