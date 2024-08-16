import os
import random
import time
from messages import message_ini, message_turn, message_winner, message_draw, dim, separator


""" Initialize the game with the players, the first one to play, and the board"""
def initialize_game():
    os.system('clear')
    message_ini()
    running = True
    players = []
    for i in range(dim):
        players.append([f"Player {i+1}", "X" if i == 0 else "O"])

    current_player = random.choice(players)
    board = []
    for i in range(dim):
        board.append(["-" for j in range(dim)])
    return players, current_player, board, running


"""Print the board and the players"""
def print_board(board, players):
    print(separator)  
    print("GAME BOARD\n")
    for row in board:
        print(row)
    
    print(f"\n{players[0][0]} : '{players[0][1]}',  {players[1][0]} : '{players[1][1]}'")
    print(separator)
    time.sleep(1)  


"""Return an array with the coordinates of the free cells"""
def free_cell_available(board):
    cells_availables = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "-":
                cells_availables.append([i, j])
    return cells_availables          
        

"""Check if the current player is the winner of the game"""
def check_winner(board, current_player):
    
    """Check row"""
    for row in board:
        if (all(cell == current_player[1] for cell in row)):
            return True
    
    """Check column"""
    for col in range(dim):
        if (all(board[row][col] == current_player[1] for row in range(dim))):
            return True    
        
    """Check diagonal1"""
    if all(board[cell][cell] == current_player[1] for cell in range(dim)):
        return True
   
    """Check diagonal2"""
    if all(board[cell][dim-1-cell] == current_player[1] for cell in range(dim)):
        return True
    
    return False


"""Update the board with the current player input"""
def update_board(board, coordinate_x, coordinate_y, current_player):
    board[coordinate_y][coordinate_x] = current_player[1]
    return board


"""Check if the input is valid and set the coordinates"""
def check_and_set_input(free_cells):
    while True:
        i = int(input("Coordinate y (row) : "))
        j = int(input("Coordinate x (column) : "))
        if i in range(dim) and j in range(dim) and [i, j] in free_cells:
            return i, j
        else:
            print("Invalid coordinates")
            print(f"Available cells: {free_cells}")


"""Update the current player"""
def update_player(players, current_player):
    if current_player == players[0]:
        return players[1]
    else:
        return players[0]



"""Main function"""
players, current_player, board, running_game = initialize_game()

while running_game:
    if free_cell_available(board) == []:
        print_board(board, players)
        message_draw()
        running_game = False
        break

    print_board(board, players)
    
    message_turn(current_player, free_cell_available(board))
    coordinate_y, coordinate_x = check_and_set_input(free_cell_available(board))

    update_board(board, coordinate_x, coordinate_y, current_player)
    if not check_winner(board, current_player):
        current_player = update_player(players, current_player)
        os.system('clear')
    else:
        os.system('clear')
        running_game = False
        print_board(board, players)
        message_winner(current_player)
        break