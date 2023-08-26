import time

board = {
    "A": [1,2,3,4,5,6,7,8,9,10],
    "B": [1,2,3,4,5,6,7,8,9,10],
    "C": [1,2,3,4,5,6,7,8,9,10],
    "D": [1,2,3,4,5,6,7,8,9,10],
    "E": [1,2,3,4,5,6,7,8,9,10],
    "F": [1,2,3,4,5,6,7,8,9,10],
    "G": [1,2,3,4,5,6,7,8,9,10],
    "H": [1,2,3,4,5,6,7,8,9,10],
    "I": [1,2,3,4,5,6,7,8,9,10],
    "J": [1,2,3,4,5,6,7,8,9,10]
}

def start_game():
    print("Welcome to Battleship. Created using Python.")
    time.sleep(2.5)
    for key, value in board.items():
        print(key + " " + str(value))
    time.sleep(1)
    print("Above is the board for Battleship. You will have five ships to place. You are fighting the computer, it won't cheat :).")

start_game()
start_game()