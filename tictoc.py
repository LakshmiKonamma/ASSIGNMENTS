import numpy as np

def create_board():
    """
    Creates an empty 3x3 Tic Tac Toe board.
    """
    return np.zeros((3, 3), dtype=int)

def check_winner(board, player):
    """
    Checks if the given player has won the game.
    """
    # Check rows and columns
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True

    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False


def print_board(board):
    """
    Prints the Tic Tac Toe board in a more Pythonic way.
    """
    symbols = {0: '-', 1: '1', 2: '2'}
    for row in board:
        print(' | '.join(symbols[cell] for cell in row))
    print("\n")


def main():
    board = create_board()
    current_player = 1  # Player 1 starts

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())

            if board[row, col] == 0:
                board[row, col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                current_player = 3 - current_player  # Switch players
            else:
                print("Cell already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by a space.")
        except IndexError:
            print("Row and column numbers must be between 0 and 2.")

main()
