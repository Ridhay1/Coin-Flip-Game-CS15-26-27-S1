import random

# Game variables for the Three Strikes extension
incorrect_count = 0

while True:
    # 1. Coin picks random choice
    coin = random.choice(["heads", "tails"])

    # 2. Get user guess and input validation loop
    while True:
        guess = input("What is your guess? ").lower()
        if guess == "heads" or guess == "tails":
            break
        print("Invalid input.")

    # 3. Check if guess matches coin flip
    if guess == coin:
        print("Correct!")
        incorrect_count = 0  # Reset incorrect count on correct guess
    else:
        print("Incorrect")
        incorrect_count += 1

    # 4. Display status and check win/loss conditions
    print(f"Current incorrect guesses: {incorrect_count}/3\n")

    if incorrect_count == 3:
        print("Game Over! You hit 3 strikes.")
        break