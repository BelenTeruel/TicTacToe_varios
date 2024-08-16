
# Funciones para chequear si hay ganador, empate y actualizar jugador

def check_winner(game):
    """Check rows, columns, and diagonals for a winning condition."""
    # Check rows
    for row in game.board:
        if all(cell == game.current_player for cell in row):
            return True

    # Check columns
    for col in range(game.dim):
        if all(game.board[row][col] == game.current_player for row in range(game.dim)):
            return True

    # Check diagonal (top-left to bottom-right)
    if all(game.board[i][i] == game.current_player for i in range(game.dim)):
        return True

    # Check diagonal (top-right to bottom-left)
    if all(game.board[i][game.dim - 1 - i] == game.current_player for i in range(game.dim)):
        return True

    return False

def check_draw(game):
    """Check if all cells are filled, indicating a draw."""
    return all(all(cell != "-" for cell in row) for row in game.board)

def update_player(game):
    """Toggle the current player."""
    game.current_player = game.players[1] if game.current_player == game.players[0] else game.players[0]
    return game.current_player
