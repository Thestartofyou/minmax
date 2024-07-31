
import math

# Evaluate the board state: +1 if AI wins, -1 if human wins, 0 otherwise
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if abs(sum(row)) == 3:
            return row[0]

    for col in range(3):
        if abs(board[0][col] + board[1][col] + board[2][col]) == 3:
            return board[0][col]

    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]

    return 0

# Check if there are any moves left
def is_moves_left(board):
    for row in board:
        if 0 in row:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If maximizer has won the game
    if score == 1:
        return score

    # If minimizer has won the game
    if score == -1:
        return score

    # If no more moves and no winner
    if not is_moves_left(board):
        return 0

    # If maximizer's move
    if is_max:
        best = -math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if board[i][j] == 0:
                    # Make the move
                    board[i][j] = 1

                    # Call minimax recursively and choose the maximum value
                    best = max(best, minimax(board, depth + 1, not is_max))

                    # Undo the move
                    board[i][j] = 0
        return best

    # If minimizer's move
    else:
        best = math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if board[i][j] == 0:
                    # Make the move
                    board[i][j] = -1

                    # Call minimax recursively and choose the minimum value
                    best = min(best, minimax(board, depth + 1, not is_max))

                    # Undo the move
                    board[i][j] = 0
        return best

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    # Traverse all cells
    for i in range(3):
        for j in range(3):
            # Check if cell is empty
            if board[i][j] == 0:
                # Make the move
                board[i][j] = 1

                # Compute evaluation function for this move
                move_val = minimax(board, 0, False)

                # Undo the move
                board[i][j] = 0

                # If the value of the current move is more than the best value, update best
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage
if __name__ == "__main__":
    board = [
        [1, -1, 0],
        [0, 1, -1],
        [0, 0, 0]
    ]

    best_move = find_best_move(board)
    print(f"The best move is at position: {best_move}")
