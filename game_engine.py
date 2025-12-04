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
        if self.board[pos] == self.EMPTY and 0 <= pos < 9:
            self.board[pos] = player
            return True
        return False
    
    def get_valid_moves(self) -> list[tuple[int, int]]:
        """
        Returns a list of valid moves (empty cells) on the board.
        """
        return [i for i, symbol in enumerate (self.board) if symbol == self.EMPTY]
    
    def check_win(self) -> str | None:
        """
        Checks if there is a winner on the board.
        
        Returns 1 or -1 if there is a winner, None otherwise.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for i, j, k in winning_combinations:
            sum = self.board[i] + self.board[j] + self.board[k]
            if sum == 3:
                return self.X
            elif sum == -3:
                return self.O
        return None

    def is_full(self) -> bool:
        """
        Checks if the board is full.
        
        Returns True if the board is full, False otherwise.
        """
        return self.EMPTY not in self.board
    
    def get_state_key(self) -> tuple[int, ...]: 
        """
        Returns a hashable representation of the board state.
        """
        return tuple(self.board)
    
def simulate_game(player1, player2) -> int | None:
    """
    Simulates a game between two players.

    player1: first player (X)
    player2: second player (O)
    Returns 1 if player1 wins, -1 if player2 wins, None for a draw.
    """
    board = TicTacToeBoard() 
    current_player = player1
    current_symbol = board.X

    while board.check_win() == None and not board.is_full():
        move_pos = current_player.get_move(board,current_symbol)
        if move_pos not in board.get_valid_moves():
            return -current_symbol
        board.make_move(move_pos, current_symbol)
        if current_symbol == board.X:
            current_symbol = board.O
            current_player = player2
        else:
            current_symbol = board.X
            current_player = player1
    return board.check_win()           
            
