# Tic-Tac-Toe with colored X and O
# Install colorama if you don't have it: pip install colorama

from colorama import Fore, Style, init
init(autoreset=True)

# Board setup
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        row = ""
        for j in range(3):
            cell = board[i*3 + j]
            if cell == "X":
                row += Fore.YELLOW + "X" + Style.RESET_ALL
            elif cell == "O":
                row += Fore.WHITE + "O" + Style.RESET_ALL
            else:
                row += " "
            if j < 2:
                row += " | "
        print(row)
        if i < 2:
            print("--+---+--")
    print()

def check_win(player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    current_player = "X"
    moves = 0
    while moves < 9:
        print_board()
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[choice] != " ":
                print("Position already taken. Try again.")
                continue
            board[choice] = current_player
            moves += 1
        except (ValueError, IndexError):
            print("Invalid input. Choose 1-9.")
            continue
        
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins! 🎉")
            return
        current_player = "O" if current_player == "X" else "X"
    
    print_board()
    print("It's a tie! 🤝")

if __name__ == "__main__":
    tic_tac_toe()
