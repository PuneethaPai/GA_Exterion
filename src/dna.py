# Understands score card arrangement i.e structure
import random


class DNA(object):
    mutate_percentage = 0

    def __init__(self, structure):
        self.structure = structure

    def __eq__(self, other):
        return self.structure == other.structure

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return reduce(lambda x, y: str(x) + str(y), self.structure)

    def crossover(self, other):
        crossover_point = random.randint(0, len(self.structure))
        child_1 = DNA(structure=self.structure[:crossover_point])
        child_2 = DNA(structure=other.structure[:crossover_point])
        child_1.__regenerate(other)
        child_2.__regenerate(self)
        return child_1, child_2

    def __regenerate(self, other):
        for score_card in other.structure:
            if score_card not in self.structure:
                self.structure.append(score_card)

    def mutate(self):
        mutated_structure = self.structure[:]
        if self.__should_mutate():
            mutated_structure = self.get_a_mutated_structure()
        return DNA(structure=mutated_structure)

    def get_a_mutated_structure(self):
        mutated_structure = self.structure[:]
        index_1, index_2 = random.sample(xrange(len(self.structure)), 2)
        mutated_structure[index_1], mutated_structure[index_2] = mutated_structure[index_2], mutated_structure[index_1]
        return mutated_structure

    def __should_mutate(self):
        probability_value = random.randint(0, 100)
        return probability_value <= self.mutate_percentage
