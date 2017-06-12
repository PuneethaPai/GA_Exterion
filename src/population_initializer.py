from container import Container
from population import Population


class PopulationInitializer(object):
    def __init__(self, nucleotide, number_of_buckets_per_container):
        self.nucleotide = nucleotide
        self.number_of_buckets_per_container = number_of_buckets_per_container

    def initialize(self, size):
        containers = self.create_container(size=size)
        return Population(containers=containers)

    def create_container(self, size):
        dnas = self.nucleotide.create(size=size)
        containers = map(lambda x: Container(x, self.number_of_buckets_per_container), dnas)
        return containers
