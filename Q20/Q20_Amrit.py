# Hangman

class Hangman:
    word: str = ""
    guesses: [str] = []
    lives: int = 0

    def __init__(self, word: str, lives: int):
        self.word = word
        self.lives = lives

    def guess(self, letter: str):
        self.guesses.append(letter)
        if letter not in self.word:
            self.lives -= 1
            return False
        return True

    def get_word(self):
        return "".join([letter if letter in self.guesses else '.' for letter in self.word])

def clear():
    print("\033[2J")
    move_cursor(0, 0)


def move_cursor(x: int, y: int):
    print(f"\033[{y};{x}H", end="")


def print_at(x: int, y: int, text: str):
    move_cursor(x, y)
    print(text, end="")

# y is optional
def print_middle(text: str, mid: int, y: int = 0):
    print_at(mid - len(text) // 2, y, text)

def print_box(x: int, y: int, width: int, height: int):
    print_at(x, y, "╔" + "═" * (width - 2) + "╗")
    for i in range(height - 2):
        print_at(x, y + i + 1, "║" + " " * (width - 2) + "║")
    print_at(x, y + height - 1, "╚" + "═" * (width - 2) + "╝")


word = input("Enter a word: ").lower().replace(" ", "")
clear()

width = 80
height = 24
if input("Custom window size?") == "y":
    print("Window options:")
    width = int(input("Width: "))
    height = int(input("Height: "))

clear()

game = Hangman(word, 6)
while True:
    clear()
    mid = width // 2
    print_box(0, 1, width, height)
    print_middle("Hangman", mid)
    print_middle("Word: " + game.get_word(), mid, height // 2)
    print_middle("Lives: " + str(game.lives), mid, 2)
    print_middle("Guesses: " + ", ".join(game.guesses), mid, 3)
    print_middle("Guess a letter: ", mid, height - 1)
    guess = input()
    game.guess(guess)
    if game.lives == 0:
        clear()
        print_middle("\x1b[31mYou lost!\x1b[0m", mid, 5)
        break
    if game.get_word() == word:
        clear()
        print_middle("\x1b[32mYou won!\x1b[0m", mid, 5)
        break

