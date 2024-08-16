import customtkinter as ctk
from cTKtictactoe import TicTacToe

def main():
    root = ctk.CTk()
    root.title("Tic Tac Toe Game")
    root.geometry("700x400")
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
