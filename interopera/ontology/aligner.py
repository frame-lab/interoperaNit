import textdistance
from nltk.corpus import wordnet
from ontology.deeplearner import Deeplearner


class Aligner:
    def __init__(self, ontologies):
        self.ontologies = ontologies

    def distance_name(self, first_ontology, second_ontology):
        if textdistance.hamming(
                first_ontology.domain_name,
                second_ontology.domain_name):
            first_ontology.match_name.append(
                second_ontology.domain_name)

    def distance_subclass(self, first_ontology, second_ontology):
        for first_subclass in first_ontology.domain_subclasses:
            for second_subclass in second_ontology.domain_subclasses:
                if textdistance.hamming(first_subclass, second_subclass):
                    first_ontology.match_subclasses.append(
                        second_ontology.domain_name)

    def distance_parameter(self, first_ontology, second_ontology):
        for first_parameter in first_ontology.domain_parameters:
            for second_parameter in second_ontology.domain_parameters:
                if first_parameter['parameter'] != 'id' and textdistance.hamming(
                        first_parameter['parameter'], second_parameter['parameter']):
                    first_ontology.match_parameters.append({
                        'domain_name': second_ontology.domain_name,
                        'domain_parameter': second_parameter
                    })

    def align_distance(self):
        for i in range(len(self.ontologies)):
            for j in range(i + 1, len(self.ontologies)):
                self.distance_name(self.ontologies[i], self.ontologies[j])
                self.distance_subclass(self.ontologies[i], self.ontologies[j])
                self.distance_parameter(self.ontologies[i], self.ontologies[j])

    def synonym_name(self, first_ontology, second_ontology):
        synonyms = []
        for syn in wordnet.synsets(first_ontology.domain_name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if second_ontology.domain_name in synonyms:
            first_ontology.match_name.append(
                second_ontology.domain_name)

    def synonym_subclass(self, first_ontology, second_ontology):
        for first_subclass in first_ontology.domain_subclasses:
            synonyms = []
            for syn in wordnet.synsets(first_subclass):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
            for second_subclass in second_ontology.domain_subclasses:
                if second_subclass in synonyms:
                    first_ontology.match_subclasses.append({
                        'domain_name': second_ontology.domain_name,
                        'domain_subclass': second_subclass
                    })
                    break

    def synonym_parameter(self, first_ontology, second_ontology):
        for first_parameter in first_ontology.domain_parameters:
            synonyms = []
            for syn in wordnet.synsets(first_parameter['parameter']):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
            for second_parameter in second_ontology.domain_parameters:
                if second_parameter['parameter'] in synonyms and first_parameter['parameter'] != 'id':
                    first_ontology.match_subclasses.append({
                        'domain_name': second_ontology.domain_name,
                        'domain_parameter': second_parameter
                    })

    def align_synonym(self):
        for i in range(len(self.ontologies)):
            for j in range(i + 1, len(self.ontologies)):
                self.synonym_name(self.ontologies[i], self.ontologies[j])
                self.synonym_subclass(self.ontologies[i], self.ontologies[j])
                self.synonym_parameter(self.ontologies[i], self.ontologies[j])

    def ident_name(self, first_ontology, second_ontology):
        if first_ontology.domain_name == second_ontology.domain_name:
            first_ontology.match_name.append(
                second_ontology.domain_name)

    def ident_subclass(self, first_ontology, second_ontology):
        for subclass in second_ontology.domain_subclasses:
            if subclass in first_ontology.domain_subclasses:
                first_ontology.match_subclasses.append({
                    'domain_name': second_ontology.domain_name,
                    'domain_subclass': subclass
                })

    def ident_parameter(self, first_ontology, second_ontology):
        for first_parameter in first_ontology.domain_parameters:
            for second_parameter in second_ontology.domain_parameters:
                if first_parameter['parameter'] != 'id' and second_parameter['parameter'] == first_parameter['parameter']:
                    first_ontology.match_parameters.append({
                        'domain_name': second_ontology.domain_name,
                        'domain_parameter': second_parameter
                    })
                    break

    def align_ident(self):
        for i in range(len(self.ontologies)):
            for j in range(i + 1, len(self.ontologies)):
                self.ident_name(self.ontologies[i], self.ontologies[j])
                self.ident_subclass(self.ontologies[i], self.ontologies[j])
                self.ident_parameter(self.ontologies[i], self.ontologies[j])

    def align_match_entity(self):
        learner = Deeplearner()
        learner.make_model()
        learner._parser_input(self.ontologies)
        learner.align()
