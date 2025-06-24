import customtkinter as ctk
from tkinter import messagebox
import functions as fn
import interface as ui

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.dim = 3
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]
        self.buttons = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        self.players = ["X", "O"]
        self.current_player = self.players[0]
        ui.setup_ui(self)

    def new_game(self):
        self.current_player = self.players[0]
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                self.buttons[row][col].config(text="", fg_color="white", state=ctk.NORMAL)

    def player_input(self, row, col):
        if self.board[row][col] == "-":
            self.board[row][col] = self.current_player
            color = "blue" if self.current_player == self.players[0] else "yellow"
            self.buttons[row][col].configure(text=self.current_player, font=('Helvetica', 10, 'bold'),
                                             fg_color=color, state=ctk.DISABLED)
            if fn.check_winner(self):
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                ui.disableBoard_buttons(self)
            elif fn.check_draw(self):
                messagebox.showinfo("Tic Tac Toe", "Draw!")
                ui.disableBoard_buttons(self)
            else:
                self.current_player = fn.update_player(self)

    def help(self):
        ui.show_help(self)

    def toggle_menu(self):
        ui.toggle_menu(self)
