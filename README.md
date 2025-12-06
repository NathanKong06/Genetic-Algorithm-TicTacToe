# Genetic-Algorithm-TicTacToe

This project implements a Tic-Tac-Toe game where the AI players are trained using a genetic algorithm. The AI learns to play the game by evolving strategies over multiple generations. The Genetic Algorithm is very rudimentary and can be improved in many ways, but it serves as a basic example of how evolutionary algorithms can be applied to game playing. Using libraries like PyGad can help streamline the implementation of genetic algorithms but this project focuses on a custom implementation for educational purposes.

## Configurable Parameters

- Population Size: 100
- Number of Generations: 50
- Mutation Rate: 0.05
- Mutation Strength: 0.2
- Number of Games per Evaluation: 5
- Selection Method: Tournament Selection
- Tournament Size: 5
- Chromosome Representation: 9-length array representing board positions
- Gene Representation: Move priorities for each board position

## Files

- `game_engine.py`: Contains the implementation of the Tic-Tac-Toe game logic.
- `genetic_operators.py`: Contains the implementation of genetic algorithm operators such as selection, crossover, and mutation.
- `player.py`: Defines the AI player class and its methods for making moves.
- `main.py`: Script to execute the training process and evaluate the trained AI players.
