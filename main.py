import numpy as np
from player import GAPlayer, CHROMOSOME_LENGTH
from genetic_operators import ( calculate_fitness, selection, crossover, mutation )

POPULATION_SIZE = 100  # Number of players in each generation
NUM_GENERATIONS = 50  # Number of generations to evolve

def initialize_population(pop_size):
    """
    Creates the first generation of GAPlayer objects.
    """
    population = [GAPlayer() for _ in range(pop_size)] # Instantiate population with random players
    print(f"Initialized a population of {pop_size} players.")
    return population

def run_evolution():
    """
    The main loop that runs the Genetic Algorithm process.
    """
    population = initialize_population(POPULATION_SIZE)
    
    print("\nStarting Genetic Algorithm Evolution...")
    print("-" * 30)

    for generation in range(NUM_GENERATIONS): # Iterate through each generation
        
        fitness_scores = calculate_fitness(population) # Calculate fitness for current population
        
        # Identify best player and average fitness this generation
        best_player = max(population, key=lambda p: p.fitness)
        avg_fitness = np.mean(fitness_scores)
        
        # Output generation summary
        print(f"Generation {generation+1}/{NUM_GENERATIONS}:")
        print(f"  Best Fitness: {best_player.fitness:.2f} | Avg Fitness: {avg_fitness:.2f}")
            
        parents = selection(population, POPULATION_SIZE) # Select parents using tournament selection

        next_generation = []
        # Create next generation through crossover and mutation
        for i in range(0, POPULATION_SIZE, 2):
            parent1_chrom = parents[i].chromosome 
            parent2_chrom = parents[i+1].chromosome
            
            # Generate offspring chromosomes via crossover
            offspring1_chrom, offspring2_chrom = crossover(parent1_chrom, parent2_chrom)
            # Apply mutation to offspring chromosomes
            mutated_offspring1_chrom = mutation(offspring1_chrom)
            mutated_offspring2_chrom = mutation(offspring2_chrom)

            # Create new GAPlayer instances with mutated chromosomes
            next_generation.append(GAPlayer(mutated_offspring1_chrom))
            next_generation.append(GAPlayer(mutated_offspring2_chrom))

        # Update population to next generation
        population = next_generation
        
    print("-" * 30)
    print("\nEvolution Complete!")
    return best_player

if __name__ == "__main__":
    final_best_player = run_evolution()
    print("\n--- Final Result ---")
    print(f"The fittest player evolved has a fitness of: {final_best_player.fitness:.2f}")