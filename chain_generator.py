# -*- coding: utf-8 -*-
import re
from collections import defaultdict
from janome.tokenizer import Tokenizer
from state import State
from state_dao import StateDao


class ChainGenerator(object):

    BEGIN = u"__BEGIN_SENTENCE__"
    END = u"__END_SENTENCE__"

    def __init__(self, text):
        self.text = text


    def make_triplet_frequency(self):
        sentences = self._split_into_sentences(self.text)
        triplet_frequency = defaultdict(int)
        for sentence in sentences:
            surfaces = self._make_surfaces(sentence)
            triplets = self._make_triplets(surfaces)
            for (triplet, n) in triplets.items():
                triplet_frequency[triplet] += n
        return triplet_frequency


    def _split_into_sentences(self, text):
        delimiter = "。|．|\."
        text = re.sub(r"({0})".format(delimiter), r"\1\n", text)
        sentences = text.splitlines()
        sentences = [sentence.strip() for sentence in sentences]
        return sentences


    def _make_surfaces(self, sentence):
        surfaces = []
        tokens = Tokenizer().tokenize(sentence)
        for token in tokens:
            surfaces.append(token.surface)
        return surfaces

    def _make_triplets(self, surfaces):
        if len(surfaces) < 3:
            return {}
        triplet_frequency = defaultdict(int)
        for i in range(len(surfaces)-2):
            triplet = tuple(surfaces[i:i+3])
            triplet_frequency[triplet] += 1
        triplet_frequency[(ChainGenerator.BEGIN, surfaces[0], surfaces[1])] = 1
        triplet_frequency[(surfaces[-2], surfaces[-1], ChainGenerator.END)] = 1
        return triplet_frequency

    def save(self, triplet_frequency, init=False):
        if init:
            state_dao = StateDao()
            state_dao.delete_all()
            datas = [State(prefix1=triplet[0], prefix2=triplet[1], 
                suffix=triplet[2], frequency=frequency) 
                for (triplet, frequency) in triplet_frequency.items()]
            for data in datas:
                state_dao.create(data)


    def show(self, triplet_frequency):
        for triplet in triplet_frequency:
            print("|".join(triplet), "\t", triplet_frequency[triplet])


if __name__ == '__main__':
    file = open('original_text.txt', 'r')
    text = file.read()
    chain = ChainGenerator(text)
    triplet_frequency = chain.make_triplet_frequency()
    chain.save(triplet_frequency, True)
    file.close()
