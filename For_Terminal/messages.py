import time

separator = "\n" + "-"*50 
dim = 3

"""Messages to display during the game"""
def message_ini():
    print(separator)
    print("Welcome to Tic Tac Toe Game!")
    print(f"The game board is a {dim}x{dim} grid.")
    print("Each player will play in turn.")
    print(f"The first player to align {dim} of his symbols wins the game.")
    print("\nLet's start the game!")
    time.sleep(0.5)

def message_turn(current_player, free_cell_available):
    print(f"\t\t\t{current_player[0]} TURN")
    print(separator)
    time.sleep(0.5)
    print("Enter the coordinates of the cell you want to play.")
    print(f"Available cells are: {free_cell_available}")
    print("\nNOTE: ['row', 'column'] are the coordinates of the cell")
    print(separator)
    time.sleep(0.5)

def message_winner(current_player):
    print(f"{current_player[0]} wins!\n")
    print("END GAME")
    print(separator)

def message_draw():
    print("DRAW GAME\n")
    print ("There are no more available cells.")
    print("No one wins !\n")
    print("END GAME")
    print(separator)
    
