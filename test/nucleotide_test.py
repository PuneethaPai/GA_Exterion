import unittest

from helper import get_a_dna_with_some_structure
from nucleotide import Nucleotide
from score_card import ScoreCard


class NucleotideTest(unittest.TestCase):
    def test_nucleotides_composed_of_same_ScoreCards_are_equal(self):
        nucleotide_1 = Nucleotide(score_cards=[ScoreCard(1, 10), ScoreCard(2, 20)])
        nucleotide_2 = Nucleotide(score_cards=[ScoreCard(2, 20), ScoreCard(1, 10)])
        self.assertEquals(nucleotide_1, nucleotide_2)
        self.assertEquals(nucleotide_1.__hash__(), nucleotide_2.__hash__())

    def test_nucleotide_composed_of_different_ScoreCards_not_equal(self):
        nucleotide_1 = Nucleotide(score_cards=[ScoreCard(1, 10), ScoreCard(2, 20)])
        nucleotide_2 = Nucleotide(score_cards=[ScoreCard(3, 30), ScoreCard(4, 40)])
        self.assertNotEqual(nucleotide_1, nucleotide_2)
        self.assertNotEqual(nucleotide_1.__hash__(), nucleotide_2.__hash__())

    def test_nucleotide_create_n_random_dna(self):
        dna = get_a_dna_with_some_structure()
        nucleotide = Nucleotide(score_cards=dna.structure)
        dnas = nucleotide.create(size=10)
        self.assertEquals(len(dnas), 10)
