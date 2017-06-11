class Population(object):
    def __init__(self, containers):
        self.containers = containers
        self.fitness = self.__calculate_fitness(containers)

    def __calculate_fitness(self, containers):
        return map(lambda x: x.fitness(), containers)