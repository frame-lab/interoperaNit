from src.synonym import Synonym
from src.distancy import Distancy
from src.translation import Translation
from src.exact import Exact
from src.deep_matcher import DeepMatcher
from src.magellan import Magellan


class Aligner:
    def __init__(self, bases):
        self.bases = bases

    def align_synonym_base(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                Synonym.synonym_name(self.bases[i], self.bases[j])
                Synonym.synonym_parameter(self.bases[i], self.bases[j])

    def align_translation_base(self):
        translation = Translation()
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                translation.translation_name(
                    self.bases[i],
                    self.bases[j])
                translation.translation_parameter(
                    self.bases[i],
                    self.bases[j])

    def align_distance_base(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                Distancy.distance_name(self.bases[i], self.bases[j])
                Distancy.distance_parameter(self.bases[i], self.bases[j])

    def align_exact_base(self):
        for i in range(len(self.bases)):
            for j in range(i + 1, len(self.bases)):
                Exact.exact_name(self.bases[i], self.bases[j])
                Exact.exact_parameter(self.bases[i], self.bases[j])

    def align_synonym_entities(self):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                Synonym.synonym_entity(base, matched_base)

    def align_translation_entities(self):
        translation = Translation()
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                translation.translation_entity(base, matched_base)

    def align_distance_entities(self):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                Distancy.distance_entity(base, matched_base)

    def align_exact_entities(self):
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                Exact.exact_entity(base, matched_base)

    def align_deep_matcher_entities(self):
        deep = DeepMatcher()
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                deep.align(base, matched_base)

    def align_magellan_entities(self):
        magellan = Magellan()
        for base in self.bases:
            matched_bases = list(set([
                match_base for match_base in self.bases if match_base.name in [
                    parameter['name'] for parameter in base.match_parameters]]))
            for matched_base in matched_bases:
                magellan.align(base, matched_base)

    def get_aligned_bases(self):
        return self.bases
