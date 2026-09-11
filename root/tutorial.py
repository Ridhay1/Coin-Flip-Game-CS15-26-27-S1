import random
# Random choice between "Left" or "Right"
value = random.choice(["Left", "Right"])

# Another valid syntax for random choice
choices = ["Left", "Right"]
value = random.choice(choices)
guess = input("What is your guess?\n")

guess = guess.lower()
