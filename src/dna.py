# Understands score card arrangement i.e structure


class DNA(object):
    def __init__(self, structure):
        self.structure = structure

    def __equal__(self, other):
        return self.structure == other.structure

    def __hash__(self):
        return hash(frozenset(self.structure))
