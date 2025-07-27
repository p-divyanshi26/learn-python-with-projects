# Number Guessing Game

A fun and simple Python game where the computer randomly picks a number between 1 and 100, and the player tries to guess it. After each guess, the program gives hints until the correct number is guessed — then shows how many attempts it took!

---

##  How It Works

- The program uses the `random` module to pick a number between 1 and 100.
- The user keeps entering guesses in a loop.
- After each guess:
  - If the guess is **too high**, the program says: `Lower Number please`.
  - If the guess is **too low**, it says: `Higher Number please`.
- When the guess is **correct**, it congratulates the user and shows the number of attempts taken.

---

## 💻 Technologies Used

- Python 3.x
- Standard library only (`random`)

