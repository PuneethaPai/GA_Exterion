# Understands the solution module ie to create buckets of equal size as to holds score card in them
from itertools import islice


class Container(object):
    def __init__(self, dna, number_of_buckets):
        self.dna = dna
        self.buckets = self.__generate_buckets(dna, number_of_buckets)

    def __generate_buckets(self, dna, number_of_buckets):
        score_cards = dna.structure
        bucket_size = len(score_cards) / number_of_buckets
        iterable = iter(score_cards)
        return list(iter(lambda: tuple(islice(iterable, bucket_size)), ()))
