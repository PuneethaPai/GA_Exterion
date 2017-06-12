# Understands a list of possible solutions and to handle creation of next population


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
