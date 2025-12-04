import numpy as np
import random
from player import CHROMOSOME_LENGTH
from game_engine import simulate_game

MUTATION_RATE = 0.05  # Probability of mutation per gene
MUTATION_STRENGTH = 0.2  # Maximum mutation change per gene
NUM_GAMES_PER_EVAL = 5  # Number of games each player plays per fitness evaluation
TOURNAMENT_SIZE = 5  # Number of players competing in tournament selection

def calculate_fitness(population):
    """
    Evaluates the performance of every player by simulating games.
    Fitness is only incremented for the active player (player_A), including reverse games.
    """
    for player in population: # Reset fitness at start for all players
        player.fitness = 0.0
        
    pop_size = len(population)
    
    for i in range(pop_size):  # Iterate through each player in the population
        player_A = population[i] # Create pool of opponents excluding current player
        opponents_pool = [p for p in population if p is not player_A] # Select a subset of opponents randomly for evaluation
        opponents = random.sample(opponents_pool, min(NUM_GAMES_PER_EVAL, len(opponents_pool)))
        
        for player_B in opponents:
            result = simulate_game(player_A, player_B) # Play game with player_A as first player
            if result == 1:
                player_A.fitness += 3  # Win rewards 3 points
            elif result == -1:
                pass  # Loss rewards no points
            else:  # draw
                player_A.fitness += 1  # Draw rewards 1 point

            result = simulate_game(player_B, player_A) # Play game with player_B as first player (reverse roles)
            if result == -1:
                player_A.fitness += 3  # Win as second player
            elif result == 1:
                pass  # Loss as second player
            else:  # draw
                player_A.fitness += 1  # Draw rewards 1 point

    # Return list of fitness scores for all players
    return [p.fitness for p in population]

def selection(population, num_parents):
    """
    Uses Tournament Selection to choose parents for the next generation.
    """
    parents = []
    
    for _ in range(num_parents):
        tournament_candidates = random.sample(population, TOURNAMENT_SIZE) # Randomly select tournament candidates
        winner = max(tournament_candidates, key=lambda p: p.fitness) # Select candidate with highest fitness as winner
        parents.append(winner)
        
    return parents

def crossover(parent1_chrom, parent2_chrom):
    """
    Performs Single-Point Crossover on two parent chromosomes.
    """
    crossover_point = random.randint(1, CHROMOSOME_LENGTH - 1) # Randomly choose crossover point (not at ends)
    # Create two offspring by combining parts of parents
    offspring1_chrom = np.concatenate((parent1_chrom[:crossover_point], parent2_chrom[crossover_point:]))
    offspring2_chrom = np.concatenate((parent2_chrom[:crossover_point], parent1_chrom[crossover_point:]))
    
    return offspring1_chrom, offspring2_chrom

def mutation(chromosome):
    """
    Randomly mutates genes in the chromosome.
    """
    mutated_chrom = chromosome.copy()
    
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            change = np.random.uniform(-MUTATION_STRENGTH, MUTATION_STRENGTH) # Apply random change within mutation strength bounds
            mutated_chrom[i] += change
            mutated_chrom[i] = np.clip(mutated_chrom[i], -2.0, 2.0) # Clamp gene value to range [-2.0, 2.0]
            
    return mutated_chrom
