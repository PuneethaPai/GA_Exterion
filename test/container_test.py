import random
import unittest

from container import Container
from dna import DNA
from helper import get_a_dna_with_some_structure
from score_card import ScoreCard


class ContainerTest(unittest.TestCase):
    def test_container_to_create_buckets(self):
        dna = get_a_dna_with_some_structure()
        container = Container(dna=dna, number_of_buckets=5)
        self.assertEquals(5, len(container.buckets))

    def test_container_equality(self):
        dna1 = get_a_dna_with_some_structure()
        dna2 = get_a_dna_with_some_structure()
        self.assertNotEqual(dna1, dna2)
        container1 = Container(dna1, 5)
        container2 = Container(dna2, 5)
        self.assertEquals(container1, container2)
        self.assertEquals(container1.__hash__(), container2.__hash__())

    def test_container_inequality(self):
        dna1 = DNA([ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA([ScoreCard(3, 30), ScoreCard(4, 40)])
        self.assertNotEqual(dna1, dna2)
        container1 = Container(dna1, 1)
        container2 = Container(dna2, 1)
        self.assertNotEqual(container1, container2)
        self.assertNotEqual(container1.__hash__(), container2.__hash__())

    def test_container_to_calculate_fitness(self):
        dna = get_a_dna_with_some_structure()
        container = Container(dna, 5)
        self.assertEquals(container.fitness(), -3200)

    def test_container_for_crossover(self):
        DNA.mutate_percentage = 50
        dna_1 = get_a_dna_with_some_structure()
        dna_2 = get_a_dna_with_some_structure()
        random.shuffle(dna_2.structure)
        self.assertNotEqual(dna_1, dna_2)
        container_1 = Container(dna=dna_1, number_of_buckets=5)
        container_2 = Container(dna=dna_2, number_of_buckets=5)
        child_container_1, child_container_2 = container_1.crossover(container_2)
        self.assertFalse(container_1.__eq__(child_container_1))
        self.assertFalse(container_2.__eq__(child_container_2))
        self.assertFalse(child_container_1.__eq__(child_container_2))
