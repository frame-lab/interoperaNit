from src.techniques.synonym import Synonym
from src.techniques.distancy import Distancy
from src.techniques.translation import Translation
from src.techniques.exact import Exact
from src.techniques.deep_matcher import DeepMatcher
from src.techniques.magellan import Magellan


class Aligner:
    def __init__(self, bases):
        self.bases = bases

    def align_base(self, name_function, parameter_function):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                name_function(self.bases[i], self.bases[j])
                parameter_function(self.bases[i], self.bases[j])

    def align_synonym_base(self):
        self.align_base(Synonym.synonym_name, Synonym.synonym_parameter)

    def align_translation_base(self):
        translation = Translation()
        self.align_base(
            translation.translation_name,
            translation.translation_parameter)

    def align_distance_base(self):
        self.align_base(Distancy.distance_name, Distancy.distance_parameter)

    def align_exact_base(self):
        self.align_base(Exact.exact_name, Exact.exact_parameter)

    def align_entities(self, entity_function):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                entity_function(base, matched_base)

    def align_synonym_entities(self):
        self.align_entities(Synonym.synonym_entity)

    def align_translation_entities(self):
        translation = Translation()
        self.align_entities(translation.translation_entity)

    def align_distance_entities(self):
        self.align_entities(Distancy.distance_entity)

    def align_exact_entities(self):
        self.align_entities(Exact.exact_entity)

    def align_deep_matcher_entities(self):
        deep = DeepMatcher()
        self.align_entities(deep.align)

    def align_magellan_entities(self):
        magellan = Magellan()
        self.align_entities(magellan.align)

    def get_aligned_bases(self):
        return self.bases
