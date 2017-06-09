import unittest

from container import Container
from dna import DNA
from score_card import ScoreCard


class ContainerTest(unittest.TestCase):
    def test_container_to_create_buckets(self):
        dna = self.get_a_dna_with_some_structure()
        container = Container(dna=dna, number_of_buckets=5)
        self.assertEquals(5, len(container.buckets))

    def test_container_equality(self):
        dna1 = self.get_a_dna_with_some_structure()
        dna2 = self.get_a_dna_with_some_structure()
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
        dna = self.get_a_dna_with_some_structure()
        container = Container(dna, 5)
        self.assertEquals(container.fitness(), -3200)

    def get_a_dna_with_some_structure(self):
        cards = [ScoreCard(1, 10), ScoreCard(2, 20),
                 ScoreCard(3, 30), ScoreCard(4, 40),
                 ScoreCard(5, 50), ScoreCard(6, 60),
                 ScoreCard(7, 70), ScoreCard(8, 80),
                 ScoreCard(9, 90), ScoreCard(10, 100)]
        return DNA(structure=cards)
