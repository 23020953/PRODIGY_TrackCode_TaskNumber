import random

MIN_GUESS = 1
MAX_GUESS = 100

def play_guessing_game(min_val: int = MIN_GUESS, max_val: int = MAX_GUESS) -> None:
    """Run the guessing game using the provided inclusive range."""
    secret_number = random.randint(min_val, max_val)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print(f"I have selected a number between {min_val} and {max_val}.")

    while True:
        
        guess = int(input(f"Enter your guess ({min_val}-{max_val}): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("🎉 Congratulations! You guessed the number correctly.")
            print(f"It took you {attempts} attempts to win the game.")
            break

if __name__ == "__main__":
    play_guessing_game()