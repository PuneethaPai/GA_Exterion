import unittest

from container import Container
from dna import DNA
from score_card import ScoreCard


class ContainerTest(unittest.TestCase):
    def test_container_to_create_buckets(self):
        dna = self.get_a_dna_with_some_structure()
        container = Container(dna=dna, number_of_buckets=5)
        self.assertEquals(5, len(container.buckets))

    def get_a_dna_with_some_structure(self):
        cards = [ScoreCard(1, 10), ScoreCard(2, 20)] * 5
        return DNA(structure=cards)
