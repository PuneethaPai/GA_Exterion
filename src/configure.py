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
            json_data = json.load(file)
            data = self.__dictionarify(json_data)
            return data

    def __dictionarify(self, json_data):
        data = {}
        problem_data = json_data['data']
        setup_data = json_data['setup']
        data['score_cards'] = problem_data['score_cards']
        data['number_of_buckets'] = problem_data['number_of_buckets']
        data['population_size'] = setup_data['population_size']
        data['kill_percentage'] = setup_data['kill_percentage']
        data['mutation_percentage'] = setup_data['mutation_percentage']
        return data

    def __form_nucleotide(self):
        cards = self.data['score_cards']
        score_cards = map(lambda index, value: ScoreCard(index, value), range(len(cards)), cards)
        return Nucleotide(score_cards)
