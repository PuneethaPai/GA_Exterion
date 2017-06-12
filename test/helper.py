from dna import DNA
from score_card import ScoreCard


def get_a_dna_with_some_structure():
    cards = [ScoreCard(1, 10), ScoreCard(2, 20),
             ScoreCard(3, 30), ScoreCard(4, 40),
             ScoreCard(5, 50), ScoreCard(6, 60),
             ScoreCard(7, 70), ScoreCard(8, 80),
             ScoreCard(9, 90), ScoreCard(10, 100)]
    return DNA(structure=cards)
