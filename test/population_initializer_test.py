import unittest

from helper import get_a_dna_with_some_structure
from nucleotide import Nucleotide
from population_initializer import PopulationInitializer


class PopulationInitializerTest(unittest.TestCase):
    def test_given_nucleotide_should_create_population_of_requires_size(self):
        dna = get_a_dna_with_some_structure()
        nucleotide = Nucleotide(dna.structure)
        initializer = PopulationInitializer(nucleotide, number_of_buckets_per_container=5)
        population = initializer.initialize(size=150)
        self.assertEquals(len(population.containers), 150)
