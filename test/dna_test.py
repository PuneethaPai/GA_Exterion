import unittest

from dna import DNA
from score_card import ScoreCard


class DNA_Test(unittest.TestCase):
    def test_dna_with_same_structure_are_equal(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        self.assertEquals(dna1,dna2)
        self.assertEquals(dna1.__hash__(), dna2.__hash__())

    def test_dna_with_different_structure_are_not_equal(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(2, 20), ScoreCard(1, 10)])
        self.assertNotEqual(dna1,dna2)
        self.assertNotEqual(dna1.__hash__(), dna2.__hash__())

    def test_DNA_to_give_beautiful_object_response(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        self.assertEquals(dna1.__str__(),dna2.__str__())