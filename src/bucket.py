class Bucket(object):
    def __init__(self, score_cards):
        self.score_cards = set(score_cards)

    def __eq__(self, other):
        return self.score_cards == other.score_cards

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return reduce(lambda x, y: str(x) + str(y), self.score_cards)
