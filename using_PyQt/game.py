class TicTacToeGame:
    def __init__(self):
        self.dim = 3
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]
        self.players = ["X", "O"]
        self.current_player = self.players[0]

    def new_game(self):
        self.current_player = self.players[0]
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]

    def player_input(self, row, col):
        if self.board[row][col] == "-":
            self.board[row][col] = self.current_player
            if self.check_winner():
                return f"{self.current_player} wins!"
            elif self.check_draw():
                return "Draw!"
            else:
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                return None

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True

        # Check columns
        for col in range(self.dim):
            if all(self.board[row][col] == self.current_player for row in range(self.dim)):
                return True

        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(self.dim)):
            return True
        if all(self.board[i][self.dim - 1 - i] == self.current_player for i in range(self.dim)):
            return True

        return False

    def check_draw(self):
        return all(all(cell != "-" for cell in row) for row in self.board)
