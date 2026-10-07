# ICT401 Assessment 3 - Individual Programming Project
# Student Name: Julianne Jamie Calma
# Student ID: 202571946
# Command Line Interface (CLI)

from engine import GameEngine


def choose_difficulty():
    files = {
        "1": ("easy.txt", "Easy"),
        "2": ("medium.txt", "Medium"),
        "3": ("hard.txt", "Hard"),
    }

    while True:
        print("\nChoose a difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in files:
            return files[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    engine = GameEngine(max_lives=6)
    filename, difficulty = choose_difficulty()

    if not engine.select_word(filename, difficulty):
        print(f"Error: '{filename}' is missing, broken, or contains no valid WORD|Hint records.")
        return

    print("\n=== WORD GUESSING GAME ===")
    print(f"Difficulty: {difficulty}")
    print(f"Hint: {engine.hint}")

    while not engine.is_over():
        print("\nWord:", engine.hidden_word())
        print("Lives remaining:", engine.remaining_lives)
        print("Score:", engine.score)
        print("Guessed letters:", " ".join(sorted(engine.guessed_letters)) or "None")

        guess = input("Guess one letter: ")
        valid, message = engine.guess_letter(guess)
        print(message)

        # Invalid input does not cost a life, so the loop simply asks again.
        if not valid:
            continue

    print("\n=== GAME OVER ===")
    print("Word:", engine.secret_word)
    if engine.has_won():
        print("Congratulations! You won!")
    else:
        print("You lost. Better luck next time!")
    print("Final score:", engine.score)

    if engine.save_history("CLI"):
        print("Game result saved to game_history.txt")
    else:
        print("Warning: the game finished, but history could not be saved.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
