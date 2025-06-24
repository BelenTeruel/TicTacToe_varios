import customtkinter as ctk

def setup_ui(game):
    ctk.set_appearance_mode("dark")  # Puede ser "light" o "dark"
    ctk.set_default_color_theme("blue")  # Temas disponibles: "blue", "green", "dark-blue"

    game.game_frame = ctk.CTkFrame(game.root)
    game.game_frame.pack(pady=20)

    game.controls_frame = ctk.CTkFrame(game.game_frame, fg_color="Purple1")
    game.controls_frame.pack(side='top', pady=10)

    pack_control_game(game.controls_frame, "Help", game.help)
    pack_control_game(game.controls_frame, "Menu", game.toggle_menu)
    pack_control_game(game.controls_frame, "Restart Game", game.new_game)
    pack_control_game(game.controls_frame, "Exit", game.root.destroy)

    # Board Frame & Buttons
    game.board_frame = ctk.CTkFrame(game.game_frame)
    game.board_frame.pack(pady=10)
    create_board_buttons(game)

    # Menu Frame
    game.menu_frame = ctk.CTkFrame(game.root)
    game.menu_frame.pack_forget()

    # Menu Controls
    game.controls_menu_frame = ctk.CTkFrame(game.menu_frame)
    game.controls_menu_frame.pack(side='top', pady=10)

    pack_menu_control(game.controls_menu_frame, "Help", game.help)
    pack_menu_control(game.controls_menu_frame, "Restart Game", game.new_game)
    pack_menu_control(game.controls_menu_frame, "Exit", game.root.destroy)
    pack_menu_control(game.controls_menu_frame, "X", game.toggle_menu)

def pack_control_game(parent, text, command):
    return ctk.CTkButton(parent, text=text, command=command).pack(side='left', padx=10, pady=10)

def pack_menu_control(parent, text, command):
    return ctk.CTkButton(parent, text=text, command=command).pack(pady=5)

def create_board_buttons(game):
    for row in range(game.dim):
        for col in range(game.dim):
            button = ctk.CTkButton(game.board_frame, text="", width=100, height=50, fg_color="white",
                                   font=("Helvetica", 10),  
                                   corner_radius=10,
                                   command=lambda row=row, col=col: game.player_input(row, col))
            button.grid(row=row, column=col, padx=5, pady=5)
            game.buttons[row][col] = button

def toggle_menu(game):
    if game.menu_frame.winfo_viewable():
        game.menu_frame.pack_forget()
        game.game_frame.pack()
    else:
        game.game_frame.pack_forget()
        game.menu_frame.pack()

def disableBoard_buttons(game):
    for row in range(game.dim):
        for col in range(game.dim):
            game.buttons[row][col].configure(state=ctk.DISABLED)

def show_help(game):
    help_window = ctk.CTkToplevel(game.root)
    help_window.title("Help")
    help_window.geometry("500x290")  

    custom_font = ctk.CTkFont(family="Helvetica", size=12, weight="bold")

    help_message = (
        "Welcome to Tic Tac Toe Game!\n\n"
        f"The game board is a {game.dim}x{game.dim} grid.\n"
        f"Players are {game.players[0]} and {game.players[1]}.\n"
        "Each player will play in turn.\n"
        f"The first one to align {game.dim} of his symbols wins the game.\n\n"
        "Let's start the game!"
    )

    help_label = ctk.CTkLabel(help_window, text=help_message, font=custom_font, justify="center", wraplength=450)
    help_label.pack(pady=20, padx=10)

    close_button = ctk.CTkButton(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)
