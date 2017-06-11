# Understands the solution module ie to create buckets of equal size as to holds score card in them

from itertools import islice

import numpy as np

from bucket import Bucket


class Container(object):
    def __init__(self, dna, number_of_buckets):
        self.dna = dna
        self.buckets = self.__generate_buckets(dna, number_of_buckets)

    def __eq__(self, other):
        return self.dna == other.dna and self.buckets == other.buckets

    def __hash__(self):
        return hash(frozenset(self.buckets))

    def __generate_buckets(self, dna, number_of_buckets):
        score_cards = dna.structure
        bucket_size = len(score_cards) / number_of_buckets
        iterable = iter(score_cards)
        buckets = list(iter(lambda: tuple(islice(iterable, bucket_size)), ()))
        buckets = map(lambda x: Bucket(x), buckets)
        return buckets

    def fitness(self):
        bucket_sums = map(lambda bucket: bucket.sum(), self.buckets)
        variance = np.var(bucket_sums)
        fitness = - variance
        return fitness

    def crossover(self, other):
        child_1, child_2 = self.dna.crossover(other.dna)
        child_1.mutate()
        child_2.mutate()
        number_of_buckets = len(self.buckets)
        return Container(child_1, number_of_buckets), Container(child_2, number_of_buckets)
