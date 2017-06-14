import unittest

from configure import Configure
from helper import get_a_dna_with_some_structure
from nucleotide import Nucleotide


class ConfigureTest(unittest.TestCase):
    def test_should_create_nucleotide_from_given_jsonfile(self):
        configure = Configure('test.json')
        dna = get_a_dna_with_some_structure()
        nucleotide = Nucleotide(dna.structure)
        self.assertEquals(configure.nucleotide, nucleotide)
