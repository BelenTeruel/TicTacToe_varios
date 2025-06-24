from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton, 
                             QGridLayout, QMessageBox, QMenuBar, QAction)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from game import TicTacToeGame

class TicTacToeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe Game")
        self.setGeometry(100, 100, 600, 400)
        
        self.game = TicTacToeGame()

        # Configurar la interfaz gráfica
        self._create_menu()
        self._create_game_board()

    def _create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        new_game_action = QAction("New Game", self)
        new_game_action.triggered.connect(self.new_game)
        file_menu.addAction(new_game_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")
        help_action = QAction("Help", self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

    def _create_game_board(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.board_layout = QGridLayout()
        self.main_layout.addLayout(self.board_layout)

        self.buttons = [[QPushButton("") for _ in range(self.game.dim)] for _ in range(self.game.dim)]
        for row in range(self.game.dim):
            for col in range(self.game.dim):
                button = self.buttons[row][col]
                button.setFont(QFont("Arial", 24))
                button.setFixedSize(100, 100)
                button.setStyleSheet("background-color: white; color: black; border: 1px solid black;")
                button.clicked.connect(lambda _, row=row, col=col: self.on_button_click(row, col))
                self.board_layout.addWidget(button, row, col)

    def new_game(self):
        self.game.new_game()
        for row in range(self.game.dim):
            for col in range(self.game.dim):
                button = self.buttons[row][col]
                button.setText("")
                button.setEnabled(True)
                button.setStyleSheet("background-color: white; color: black; border: 1px solid black;")

    def on_button_click(self, row, col):
        result = self.game.player_input(row, col)
        button = self.buttons[row][col]
        button.setText(self.game.current_player)
        button.setStyleSheet(f"background-color: {'blue' if self.game.current_player == 'X' else 'yellow'}; color: black; border: 1px solid black;")
        button.setEnabled(False)

        if result:
            QMessageBox.information(self, "Game Over", result)
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for row in range(self.game.dim):
            for col in range(self.game.dim):
                self.buttons[row][col].setEnabled(False)

    def show_help(self):
        help_message = (
            "Welcome to Tic Tac Toe Game!\n\n"
            f"The game board is a {self.game.dim}x{self.game.dim} grid.\n"
            f"Players are {self.game.players[0]} and {self.game.players[1]}.\n"
            "Each player will play in turn.\n"
            f"The first one to align {self.game.dim} of their symbols wins the game.\n\n"
            "Let's start the game!"
        )
        QMessageBox.information(self, "Help", help_message)
