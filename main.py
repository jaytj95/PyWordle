import colorama
from colorama import Fore, Style
import random

print("Welcome to PyWordle!")
print("Initializing...", end='')

boards = [
    [("-", 0), ("-", 0), ("-", 0), ("-", 0), ("-", 0)],
    [("-", 0), ("-", 0), ("-", 0), ("-", 0), ("-", 0)],
    [("-", 0), ("-", 0), ("-", 0), ("-", 0), ("-", 0)],
    [("-", 0), ("-", 0), ("-", 0), ("-", 0), ("-", 0)],
    [("-", 0), ("-", 0), ("-", 0), ("-", 0), ("-", 0)]
]
answer = random.choice(open('wordle-answers-alphabetical.txt').read().splitlines())
words = open('wordle-allowed-guesses.txt').read().splitlines()
print("Done!")


def print_board(game_round):
    print("Round " + str(game_round))
    for board in boards:
        for i in range(5):
            letter = board[i]
            if letter[0] == "-" or letter[1] == 0:
                color = Fore.LIGHTWHITE_EX
            elif letter[1] == 1:
                color = Fore.YELLOW
            else:
                color = Fore.GREEN
            print(color, letter[0], end=' ')
        print(Style.RESET_ALL)


def get_input():
    guess = input("Enter your value: ")
    # if guess not in words:
    #     print("Invalid word, try a different one")
    #     return get_input()
    return guess


# need to correct yellow markings: if yellow letter is solved, and there is not a duplicate, mark white
def process_guess(game_round, guess):
    board = []

    yellows = set()
    for i in range(5):
        c = guess[i]
        a = answer[i]
        # green
        if c == a:
            board.append((c, 2))
        # yellow
        elif c in answer:
            if c not in yellows:
                board.append((c, 1))
                yellows.add(c)
            else:
                board.append((c, 0))
        # white
        else:
            board.append((c, 0))
    boards[game_round - 1] = board

    return guess == answer


def play_game():
    game_round = 1
    guess = ""
    while guess != answer and game_round < 6:
        print_board(game_round)
        guess = get_input()
        process_guess(game_round, guess)
        game_round = game_round + 1


play_game()
print_board("Over!")
print("The word was " + answer)
