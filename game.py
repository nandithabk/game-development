def print_board(board):
    # Display the Tic Tac Toe board
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board, player):
    # Check if the current player has won by examining rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # Check if the Tic Tac Toe board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    # Initialize the Tic Tac Toe board and set the starting player to 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    # Main game loop
    while True:
        # Display the current state of the board
        print_board(board)

        # Get the player's move (row and column)
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        # Check if the selected cell is empty
        if board[row][col] == ' ':
            # Place the player's symbol in the selected cell
            board[row][col] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            # Check if the board is full, resulting in a tie
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                # Switch to the other player for the next turn
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            # Display a message if the selected cell is already occupied
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    # Start the Tic Tac Toe game
    tic_tac_toe()