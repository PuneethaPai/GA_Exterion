from configure import Configure
from dna import DNA
import numpy as np
from population import Population
from population_initializer import PopulationInitializer

configure = Configure('data.json')
number_of_buckets = configure.data['number_of_buckets']
population_size = configure.data['population_size']
kill_percentage = configure.data['kill_percentage']
mutation_percentage = configure.data['mutation_percentage']
Population.kill_percentage = kill_percentage
DNA.mutate_percentage = mutation_percentage
nucleotide = configure.nucleotide
initializer = PopulationInitializer(nucleotide=nucleotide, number_of_buckets_per_container=number_of_buckets)
initial_population = initializer.initialize(population_size)

populations = [initial_population]
fitness_list = [np.mean(initial_population.fitness)]
while True:
    if len(populations) >= 300 or fitness_list[-1] >= -1:
        break
    current_population = populations[-1]
    next_population = current_population.next_population()
    next_fitness = np.mean(next_population.fitness)
    populations.append(next_population)
    fitness_list.append(next_fitness)

for fitness, population in zip(fitness_list, populations):
    print population.containers[0].dna, fitness
