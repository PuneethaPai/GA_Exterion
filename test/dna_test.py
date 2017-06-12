import random
import unittest

from dna import DNA
from helper import get_a_dna_with_some_structure
from score_card import ScoreCard


class DNA_Test(unittest.TestCase):
    def test_dna_with_same_structure_are_equal(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        self.assertEquals(dna1, dna2)
        self.assertEquals(dna1.__hash__(), dna2.__hash__())

    def test_dna_with_different_structure_are_not_equal(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(2, 20), ScoreCard(1, 10)])
        self.assertNotEqual(dna1, dna2)
        self.assertNotEqual(dna1.__hash__(), dna2.__hash__())

    def test_DNA_to_give_beautiful_object_response(self):
        dna1 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        dna2 = DNA(structure=[ScoreCard(1, 10), ScoreCard(2, 20)])
        self.assertEquals(dna1.__str__(), dna2.__str__())

    def test_dna_crossover_with_itself_gives_same_two_children(self):
        dna = get_a_dna_with_some_structure()
        child_1, child_2 = dna.crossover(dna)
        self.assertEquals(child_1, child_2)

    def test_dna_crossover_to_get_two_children(self):
        dna1 = get_a_dna_with_some_structure()
        dna2 = get_a_dna_with_some_structure()
        random.shuffle(dna2.structure)
        child_1, child_2 = dna1.crossover(dna2)
        self.assertNotEqual(child_1, child_2)

    def test_dna_mutation_with_zero_percent_gives_same_dna(self):
        DNA.mutate_percentage = 0
        original = get_a_dna_with_some_structure()
        mutated = original.mutate()
        self.assertEqual(original, mutated)

    def test_dna_mutation_with_hundred_percent_gives_mutated_dna(self):
        DNA.mutate_percentage = 100
        original = get_a_dna_with_some_structure()
        mutated = original.mutate()
        self.assertNotEqual(original, mutated)
