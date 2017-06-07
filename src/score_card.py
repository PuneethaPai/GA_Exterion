# Understands a place holder for a value


class ScoreCard(object):
    def __init__(self, index, score):
        self.index = index
        self.score = score

    def __eq__(self, other):
        return self.index == other.index and self.score == other.score

    def __hash__(self):
        return hash(self.index) + 1303 * hash(self.score)

    def __str__(self):
        return '{index : %s, score: %s}' %(self.index, self.score)