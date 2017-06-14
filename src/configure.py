import json
import os

from definations import ASSETS
from nucleotide import Nucleotide
from score_card import ScoreCard


class Configure(object):
    def __init__(self, json_file):
        self.data = self.__read(json_file)
        self.nucleotide = self.__form_nucleotide()

    def __read(self, json_file):
        path = os.path.join(ASSETS, json_file)
        with open(path, 'rb') as file:
            data = json.load(file)
            return data

    def __form_nucleotide(self):
        cards = self.data['score_cards']
        score_cards = map(lambda index, value: ScoreCard(index, value), range(len(cards)), cards)
        return Nucleotide(score_cards)
