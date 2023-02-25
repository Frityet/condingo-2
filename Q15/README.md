# CBO Coding Challenge Question 15 - 4 points

Create an interactive game in the terminal with the following technical spec (specification)

1. When the game starts, the terminal should generate a random number. For this, you can use the random module.
1a. To generate a number, you can use the code `random.randint(1, 100)`, which means that the `random` module will generate a number between 1 and 100. Remember to import the module at the top of your file. https://docs.python.org/3/library/random.html
2. The player should have 7 "lives", or chances at guessing
3. If the player does not guess the number correctly, the prompt should guide the user in the direction of the number (either higher or lower)
4. The game should run until the player either has no more lives or guesses the number correctly
