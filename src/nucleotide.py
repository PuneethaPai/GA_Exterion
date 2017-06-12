import random

from dna import DNA


class Nucleotide(object):
    def __init__(self, score_cards):
        self.score_cards = set(score_cards)

    def __eq__(self, other):
        return self.score_cards == other.score_cards

    def __hash__(self):
        return hash(frozenset(self.score_cards))

    def create(self, size):
        return map(lambda x: self.generate_a_dna(), xrange(size))

    def generate_a_dna(self):
        return DNA(random.sample(self.score_cards, len(self.score_cards)))
