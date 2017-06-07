import unittest

from score_card import ScoreCard


class ScoreCardTest(unittest.TestCase):
    def test_cards_with_same_parameter_are_equal(self):
        score_card1 = ScoreCard(index=1, score=10)
        score_card2 = ScoreCard(index=1, score=10)
        self.assertTrue(score_card1.__eq__(score_card2))
        self.assertEquals(score_card1.__hash__(), score_card2.__hash__())

    def test_cards_with_different_parameter_are_not_equal(self):
        score_card1 = ScoreCard(index=1, score=10)
        score_card2 = ScoreCard(index=2, score=20)
        self.assertFalse(score_card1.__eq__(score_card2))
        self.assertNotEqual(score_card1.__hash__(), score_card2.__hash__())