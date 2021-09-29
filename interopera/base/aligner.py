from base.synonym import Synonym
from base.distancy import Distancy
from base.translation import Translation
from base.deeplearner import Deeplearner


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
        learner.make_model()
        learner._parser_input(self.bases)
        learner.align()
