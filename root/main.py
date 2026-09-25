import random

incorrect_count = 0

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("What is your guess? ").lower()
        if guess == "heads" or guess == "tails":
            break
        print("Invalid input.")

    if guess == coin:
        print("Correct!")
        incorrect_count = 0
    else:
        print("incorrect")
        incorrect_count += 1

    print(f"Current incorrect guesses: {incorrect_count}")

    if incorrect_count == 3:
        print("game Over! You hit 3 strikes try again later!.")
        break