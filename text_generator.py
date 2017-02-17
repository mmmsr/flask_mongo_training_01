# -*- coding: utf-8 -*-
import os.path
import random
from chain_generator import ChainGenerator
from state import State
from state_dao import StateDao
import settings


class TextGenerator(object):
    def __init__(self, number_of_sentences=settings.NUMBER_OF_SENTENCES):
        self.number_of_sentences = number_of_sentences


    def generate(self, keyword=settings.DEFAULT_KEYWORD):
        text = u""
        for i in range(self.number_of_sentences):
            text += self._generate_sentence()
        text = text.replace(settings.KEYWORD_REPLASED, keyword)
        return text


    def _generate_sentence(self):
        morphemes = []
        first_triplet = self._get_first_state()
        morphemes.append(first_triplet[1])
        morphemes.append(first_triplet[2])
        while morphemes[-1] != ChainGenerator.END:
            prefix1 = morphemes[-2]
            prefix2 = morphemes[-1]
            triplet = self._make_triplet(prefix1, prefix2)
            morphemes.append(triplet[2])
        sentence = "".join(morphemes[:-1])
        return sentence


    def _get_first_state(self):
        prefixes = (ChainGenerator.BEGIN,)
        states = self._get_states_from_db(prefixes)
        triplet = self._choose_triplet_at_random(states)
        return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])


    def _get_states_from_db(self, prefixes):
        state_dao = StateDao()
        if len(prefixes) == 2:
            datas = state_dao.read(prefix1=prefixes[0], prefix2=prefixes[1])
        elif len(prefixes) == 1:
            datas = state_dao.read(prefix1=prefixes[0], prefix2=None)
        states = []
        for data in datas:
            states.append(dict(data))
        return states


    def _make_triplet(self, prefix1, prefix2):
        prefixes = (prefix1, prefix2)
        states = self._get_states_from_db(prefixes)
        triplet = self._choose_triplet_at_random(states)
        return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])


    def _choose_triplet_at_random(self, states):
        probability = []
        for (index, state) in enumerate(states):
            for j in range(state["frequency"]):
                probability.append(index)
        state_index = random.choice(probability)
        return states[state_index]


if __name__ == '__main__':
    text_generator = TextGenerator()
    print(text_generator.generate())
