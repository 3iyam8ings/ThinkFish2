# we have installed python lib using "pip install python-chess requests pytest" that is why import chess
import chess

def main():
    # Create a new chessboard
    board = chess.Board()
    print("WELCOME TO THINKFISH2")
    print("=====================")
    print(board)

    print("\nAvailable legal moves:")

    for move in board.legal_moves:
        print(move)
    # Executes White's pawn move to e4 using SAN notation.
    board.push_san("e4")

    print("\nBoard after White plays e4:")
    print(board)
    # Display FEN(represents a single chessboard position)
    print("\nCurrent FEN:")
    print(board.fen())

#Checks whether the Python file is being executed directly.
if __name__ == "__main__":
    main()