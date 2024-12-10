# Tic-Tac-Toe game in Python

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--------")
    print()

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def main():
    # Initial empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get valid player input
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
                if row not in range(3) or col not in range(3) or board[row][col] != " ":
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter row and column as two numbers between 0 and 2, and ensure the cell is empty.")
        
        # Make the move
        board[row][col] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
