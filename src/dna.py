# Understands score card arrangement i.e structure


class DNA(object):
    def __init__(self, structure):
        self.structure = structure

    def __eq__(self, other):
        return self.structure == other.structure

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return reduce(lambda x, y: str(x) + str(y), self.structure)
