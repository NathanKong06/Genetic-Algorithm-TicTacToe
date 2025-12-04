class TicTacToeBoard:
    def __init__(self):
        """
        Creates the board as a 1D list. 0 indicates an empty cell, 1 indicates 'X', and -1 indicates 'O'.
        """
        self.board = [0] * 9 # [0,0,0,0,0,0,0,0,0]
        self.EMPTY = 0
        self.X = 1
        self.O = -1

    def make_move(self, pos, player) -> bool:
        """
        Makes a move on the board at a given position for a player.
        
        player (str): 1 or -1
        pos (int): position from 0 to 8
        Returns True if move was made, False otherwise.
        """
        if 0 <= pos < 9 and self.board[pos] == self.EMPTY: # Check if position is within bounds and empty
            self.board[pos] = player  # Place player's mark on the board
            return True
        return False
    
    def get_valid_moves(self) -> list[int]:
        """
        Returns a list of valid moves (empty cells) on the board.
        """
        return [i for i, symbol in enumerate(self.board) if symbol == self.EMPTY] # Return indices of all empty cells
    
    def check_win(self) -> str | None:
        """
        Checks if there is a winner on the board.
        
        Returns 1 or -1 if there is a winner, None otherwise.
        """
        # List all possible winning triplets of indices
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for i, j, k in winning_combinations: # Check each winning combination
            cur_sum = self.board[i] + self.board[j] + self.board[k]
            if cur_sum == 3:
                return self.X  # Player X wins
            elif cur_sum == -3:
                return self.O  # Player O wins
        return None  # No winner yet

    def is_full(self) -> bool:
        """
        Checks if the board is full.
        
        Returns True if the board is full, False otherwise.
        """
        return self.EMPTY not in self.board  # If no empty cells, board is full
    
def simulate_game(player1, player2) -> int | None:
    """
    Simulates a game between two players.

    player1: first player (X)
    player2: second player (O)
    Returns 1 if player1 wins, -1 if player2 wins, None for a draw.
    """
    board = TicTacToeBoard()  # Initialize new game board
    current_player = player1
    current_symbol = board.X  # Player1 uses X (1)

    while board.check_win() == None and not board.is_full(): # Continue until a win or board is full (draw)
        move_pos = current_player.get_move(board) # Get move from current player
        if move_pos not in board.get_valid_moves(): # Check if move is valid
            return -current_symbol  # Penalize illegal move by returning opponent's win
        board.make_move(move_pos, current_symbol)  
        if current_symbol == board.X: # Switch player and symbol for next turn
            current_symbol = board.O
            current_player = player2
        else:
            current_symbol = board.X
            current_player = player1
    return board.check_win() # Return the winner or None if draw