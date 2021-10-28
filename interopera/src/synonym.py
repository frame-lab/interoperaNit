from nltk.corpus import wordnet


class Synonym:
    @staticmethod
    def synonym_name(base, base_candidate):
        synonyms = []
        for syn in wordnet.synsets(base.name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if base_candidate.name in synonyms and \
                base_candidate.name not in base.match_name:
            base.match_name.append(
                base_candidate.name)

    @staticmethod
    def synonym_parameter(base, base_candidate):
        for base_parameter in base.parameters:
            synonyms = []
            for syn in wordnet.synsets(base_parameter['parameter']):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())

            for base_candidate_parameter in base_candidate.parameters:
                match_parameter = {
                    'name': base_candidate.name,
                    'matched_parameter': base_candidate_parameter,
                    'my_parameter': base_parameter
                }

                if base_candidate_parameter['parameter'] in synonyms \
                        and base_parameter['parameter'] != 'id' and \
                        match_parameter not in base.match_parameters:

                    base.match_parameters.append(match_parameter)
