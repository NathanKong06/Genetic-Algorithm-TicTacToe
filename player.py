import numpy as np

CHROMOSOME_LENGTH = 9  # Number of genes representing moves on the board

class GAPlayer:
    """
    Represents a single player (chromosome) using a NumPy array for its strategy weights.
    """
    def __init__(self, chromosome=None):
        if chromosome is None: # Initialize chromosome with random weights if none provided
            self.chromosome = np.random.uniform(-1.0, 1.0, CHROMOSOME_LENGTH)
        else:
            self.chromosome = np.array(chromosome) 
            
        self.fitness = 0.0  # Initialize fitness score

    def get_move(self, board):
        """
        Decides the best move based on the current board state and the player's weights.
        
        """
        valid_moves = board.get_valid_moves()  # Get available moves
        if not valid_moves:
            return -1  # No valid moves available

        best_move = valid_moves[0]  # Initialize best move
        best_score = -np.inf  # Initialize best score to negative infinity

        for move in valid_moves: # Evaluate each valid move based on chromosome weights
            current_score = self.chromosome[move] 

            if current_score > best_score:
                best_score = current_score
                best_move = move
                
        return best_move  # Return move with highest weight