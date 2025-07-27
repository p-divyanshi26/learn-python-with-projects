import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    a = int(input("Guess a number: "))
    guesses += 1

    if a > n:
        print("Lower Number please")
    elif a < n:
        print("Higher Number please")
    else:
        print(f"You have guessed the number {n} correctly in {guesses} attempts!")
