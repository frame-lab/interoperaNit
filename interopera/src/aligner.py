from interopera.src.synonym import Synonym
from interopera.src.distancy import Distancy
from interopera.src.translation import Translation
from interopera.src.deeplearner import Deeplearner


class Aligner:
    def __init__(self, bases):
        self.bases = bases

    def align_synonym(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                Synonym.synonym_name(self.bases[i], self.bases[j])
                Synonym.synonym_parameter(self.bases[i], self.bases[j])

    def align_translation(self):
        translation = Translation()
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                translation.translation_name(
                    self.bases[i],
                    self.bases[j])
                translation.translation_parameter(
                    self.bases[i],
                    self.bases[j])

    def align_distance(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                Distancy.distance_name(self.bases[i], self.bases[j])
                Distancy.distance_parameter(self.bases[i], self.bases[j])

    def align_match_entity(self):
        learner = Deeplearner()
        learner.parser_input(self.bases)
        learner.align()
