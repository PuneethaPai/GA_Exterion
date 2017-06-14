from dna import DNA
from score_card import ScoreCard


def get_a_dna_with_some_structure():
    cards = [ScoreCard(0, 10), ScoreCard(1, 20),
             ScoreCard(2, 30), ScoreCard(3, 40),
             ScoreCard(4, 50), ScoreCard(5, 60),
             ScoreCard(6, 70), ScoreCard(7, 80),
             ScoreCard(8, 90), ScoreCard(9, 100)]
    return DNA(structure=cards)
