from nltk.corpus import wordnet


class Synonym:
    @staticmethod
    def synonym_name(base_name, base_candidate_name):
        synonyms = []
        for syn in wordnet.synsets(base_name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        return base_candidate_name in synonyms

    @staticmethod
    def synonym_parameter(base_parameter, base_candidate_parameter):
        synonyms = []
        for syn in wordnet.synsets(base_parameter):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        return base_candidate_parameter in synonyms

    @staticmethod
    def synonym_entity(base_entity, matched_base_entity):
        synonyms = []
        for syn in wordnet.synsets(base_entity):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        return matched_base_entity not in synonyms
