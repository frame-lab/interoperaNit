from sqlalchemy import false
from src.techniques.synonym import Synonym
from src.techniques.distancy import Distancy
from src.techniques.translation import Translation
from src.techniques.exact import Exact
from src.techniques.deep_matcher import DeepMatcher
from src.techniques.magellan import Magellan
from src.techniques.techniques import Techniques


class Aligner:
    def __init__(self, bases, verbose):
        self.bases = bases
        self.verbose = verbose

    def align_base(self, comparison_function):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                if self.verbose:
                    print(
                        f'Making alignment of the parameters from bases {self.bases[i].name} and {self.bases[j].name}')
                Techniques.techniques_name(
                    self.bases[i], self.bases[j], comparison_function)
                Techniques.techniques_parameter(
                    self.bases[i], self.bases[j], comparison_function, self.verbose)

    def align_synonym_base(self):
        self.align_base(Synonym.synonym_comparison)

    def align_translation_base(self):
        translation = Translation()
        self.align_base(translation.translation_comparison)

    def align_distance_base(self):
        self.align_base(Distancy.distancy_comparison)

    def align_exact_base(self):
        self.align_base(Exact.exact_comparison)

    def align_entities(self, comparison_function, comparison_type, should_approximate):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                if(self.verbose):
                    print(
                        f'Making alignment of the entities from bases {base.name} and {matched_base.name}')
                Techniques.techniques_entity(
                    base, matched_base, comparison_function, comparison_type, should_approximate, self.verbose)

    def align_entities_max(self, value_function):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                if(self.verbose):
                    print(
                        f'Making alignment of the entities from bases {base.name} and {matched_base.name}')
                Techniques.techniques_entity_max(
                    base, matched_base, value_function, self.verbose)

    def align_synonym_entities(self):
        self.align_entities(Synonym.synonym_comparison, 'not', True)

    def align_translation_entities(self):
        translation = Translation()
        self.align_entities(translation.translation_comparison, 'not', True)

    def align_distance_entities(self, max):
        if max:
            self.align_entities_max(Distancy.distancy_value)
        else:
            self.align_entities(Distancy.distancy_comparison, 'le', True)

    def align_exact_entities(self):
        self.align_entities(Exact.exact_comparison, 'ne', False)

    def align_entities_ia(self, ia_function):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                if(self.verbose):
                    print(
                        f'Making alignment of the entities from bases {base.name} and {matched_base.name}')
                ia_function(base, matched_base)

    def align_deep_matcher_entities(self):
        deep = DeepMatcher()
        self.align_entities_ia(deep.align)

    def align_magellan_entities(self):
        magellan = Magellan()
        self.align_entities_ia(magellan.align)

    def get_aligned_bases(self):
        return self.bases
