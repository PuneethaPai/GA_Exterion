# Understands a list of possible solutions and to handle creation of next population
import random


class Population(object):
    kill_percentage = 0

    def __init__(self, containers):
        self.containers = containers
        self.fitness = self.__calculate_fitness(containers)
        self.sort_containers_based_on_fitness()

    def __calculate_fitness(self, containers):
        return map(lambda x: x.fitness(), containers)

    def sort_containers_based_on_fitness(self):
        sorted_tuples = sorted(zip(self.fitness, self.containers))
        sorted_tuples = sorted_tuples[::-1]
        self.fitness = map(lambda x: x[0], sorted_tuples)
        self.containers = map(lambda x: x[1], sorted_tuples)

    def next_population(self):
        kill_index = len(self.containers) * self.kill_percentage / 100
        survivor_index = len(self.containers) - kill_index
        survivors = self.containers[:survivor_index]
        new_containers = self.__generate_next_descendents_from(survivors)
        return Population(containers=new_containers)

    def __generate_next_descendents_from(self, survivors):
        new_containers = survivors[:]
        while len(new_containers) < len(self.containers):
            parent_1, parent_2 = self.__get_random_parent(survivors)
            child_1, child_2 = parent_1.crossover(parent_2)
            new_containers.append(child_1)
            new_containers.append(child_2)
        return new_containers

    def __get_random_parent(self, survivors):
        parents = random.sample(survivors, 2)
        return parents
