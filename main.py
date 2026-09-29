import random
number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100")
print("Level 1: easy, 15 guesses")
print("Level 2: medium, 10 guesses")
print("Level 3: hard, 5 guesses")

level = input("Enter 1, 2, or 3: ")
max_attempts = {"1": 15, "2": 10, "3": 5}.get(level, 10)
if level not in {"1", "2", "3"}:
    print("Invalid choice; using medium level.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    attempts += 1
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    if guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print(f"You lost. The number was {number}.")