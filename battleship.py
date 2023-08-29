import time
import random

# Classes
class Board:
    def __init__(self,iname):
        self.name = iname
        self.brd = {
            " ": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "A": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "B": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "C": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "D": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "E": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "F": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "G": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "H": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "I": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "J": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
    
    def show_board(self):
        for key, value in self.brd.items():
            print(key + str(value))

    def access_element(self, row, col):
        return self.brd[row][col]     
               
    def modify_element(self, row, col, value):
        self.brd[row][col] = value    
    
    def generate_board(self):
        for ship_size in range(1, 5):
            while True:
                ori = random.choice(['hori', 'vert'])
                
                if ori == 'hori':
                    row = random.choice(list(self.brd.keys()))
                    col = random.randint(0, 11 - ship_size)
                    
                    if col + ship_size <= 10:
                        valid_placement = all(self.brd[row][col + i] == 0 for i in range(ship_size))
                        if valid_placement:
                            for i in range(ship_size):
                                self.brd[row][col + i] = 1
                            break
                else:
                    valid_rows = list(self.brd.keys())[1:12 - ship_size]
                    row_index = random.randint(0, len(valid_rows) - ship_size)
                    row = valid_rows[row_index]
                    col = random.randint(0, 10)
                    
                    if ord(row) + ship_size - 1 <= ord('K'):
                        valid_placement = all(self.brd[chr(ord(row) + i)][col] == 0 for i in range(ship_size))
                        if valid_placement:
                            for i in range(ship_size):
                                self.brd[chr(ord(row) + i)][col] = 1
                            break
         

# Base variables and initilizing
game_won = False
Computer = Board("Computer")
Base = Board("Base")
i1 = input("What is your name? ")
Player = Board(i1)

# Functions

# This function is not necessarily needed but it improves code readability
def start_game():
    print("Welcome to Battleship, "+ Player.name +"! Created using Python.")
    time.sleep(1)
    Player.show_board()
    time.sleep(1)
    print("Above is the board for Battleship. You are fighting the computer, it won't cheat :).")
    time.sleep(1)
    print("Each game randomly generates the positions of the ships. Your board is generating...")
    Player.generate_board()
    Computer.generate_board()
    Base.show_board()
    print(" ")
    print("Enemy Board /\ Player Board \/")
    print(" ")
    Player.show_board()
    time.sleep(0.5)
    print("To start attacking, you will be asked to enter in a row letter then a column number.")
    time.sleep(0.25)


def place_move(Player, Computer, Base):
    global game_won
    count = 0
    while not game_won:
        if count % 2 == 0:
            in1 = input("Which row letter? ")
            in2 = int(input("Which column number? "))
            if in1 in Computer.brd and 0 <= in2 <= 9:  
                if Computer.access_element(in1, in2) == 1:
                    Base.modify_element(in1, in2, 'X')
                    Computer.modify_element(in1, in2, 'X')
                    Computer.show_board()
                    print("Ship hit!")
                elif Computer.access_element(in1, in2) == 0:
                    Base.modify_element(in1, in2, 'M')
                    Computer.modify_element(in1, in2, 'M')
                    Computer.show_board()
                    print("Miss!")
            else:
                print("Invalid input. Please enter a valid row letter (A-J) and column number (0-9).")
        else:
            a = random.choice(list(Player.brd.keys()))
            b = random.randint(0,9)
            if Player.access_element(a,b) == 1:
                Player.modify_element(a,b, 'X')
                print("The computer hit you!")
            elif Player.access_element(a,b) == 0:
                Player.modify_element(a,b, 'M')
                print("The computer missed you!")

        
        if all(value == 'X' or value == 'M' or value == 0 for row in Computer.brd.values() for value in row):
            print(Player.name + " has won the game!")
            game_won = True
            break

        if all(value == 'X' or value == 'M' or value == 0 for row in Player.brd.values() for value in row):
            print("The computer has won the game!")
            game_won = True
            break

        count += 1

start_game()
place_move(Player, Computer, Base)