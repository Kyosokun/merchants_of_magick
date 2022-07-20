from game import Game
from game_loop import game_loop


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game(3)
    game_loop(game)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
