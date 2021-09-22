import textdistance
from nltk.corpus import wordnet
from base.deeplearner import Deeplearner


class Aligner:
    def __init__(self, bases):
        self.bases = bases

    def synonym_name(self, first_base, second_base):
        synonyms = []
        for syn in wordnet.synsets(first_base.name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if second_base.name in synonyms:
            first_base.match_name.append(
                second_base.name)

    def synonym_parameter(self, first_base, second_base):
        for first_parameter in first_base.parameters:
            synonyms = []
            for syn in wordnet.synsets(first_parameter['parameter']):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
            for second_parameter in second_base.parameters:
                if second_parameter['parameter'] in synonyms and first_parameter['parameter'] != 'id':
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })

    def align_synonym(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                self.synonym_name(self.bases[i], self.bases[j])
                self.synonym_parameter(self.bases[i], self.bases[j])

    def translation_name(self, first_base, second_base):
        synonyms = []
        for syn in wordnet.synsets(first_base.name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if second_base.name in synonyms:
            first_base.match_name.append(
                second_base.name)

    def translation_parameter(self, first_base, second_base):
        for first_parameter in first_base.parameters:
            synonyms = []
            for syn in wordnet.synsets(first_parameter['parameter']):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
            for second_parameter in second_base.parameters:
                if second_parameter['parameter'] in synonyms and first_parameter['parameter'] != 'id':
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })

    def align_translation(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                self.translation_name(self.bases[i], self.bases[j])
                self.translation_parameter(self.bases[i], self.bases[j])

    def distance_name(self, first_base, second_base):
        if textdistance.hamming.normalized_similarity(
                first_base.name,
                second_base.name) > 0.75:
            first_base.match_name.append(
                second_base.name)

    def distance_parameter(self, first_base, second_base):
        for first_parameter in first_base.parameters:
            for second_parameter in second_base.parameters:
                if first_parameter['parameter'] != 'id' and textdistance.hamming.normalized_similarity(
                        first_parameter['parameter'], second_parameter['parameter']) > 0.75:
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })

    def align_distance(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                self.distance_name(self.bases[i], self.bases[j])
                self.distance_parameter(self.bases[i], self.bases[j])

    def align_match_entity(self):
        learner = Deeplearner()
        learner.make_model()
        learner._parser_input(self.bases)
        learner.align()
