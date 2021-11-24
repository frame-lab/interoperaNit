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
                    'my_parameter': base_parameter,
                    'approximate': base_parameter['approximate'] and base_candidate_parameter['approximate']
                }

                if base_parameter['unique'] and base_candidate_parameter['parameter'] in synonyms \
                        and base_parameter['parameter'] != 'id' and \
                        match_parameter not in base.match_parameters:

                    base.match_parameters.append(match_parameter)

    @staticmethod
    def synonym_entity(base, matched_base):
        match_params = [parameter for parameter in base.match_parameters
                        if parameter['name'] == matched_base.name and parameter['approximate']]

        base_param_indexes = []
        matched_param_indexes = []

        for match_param in match_params:
            base_parameter = match_param["my_parameter"]
            matched_base_parameter = match_param["matched_parameter"]

            base_param_indexes.append(
                base.parameters.index(base_parameter))
            matched_param_indexes.append(
                matched_base.parameters.index(matched_base_parameter))

        for base_index in range(0, len(base.entities)):
            for matched_base_index in range(0, len(matched_base.entities)):
                is_match = True
                for param_index in range(0, len(base_param_indexes)):
                    synonyms = []
                    for syn in wordnet.synsets(
                            base.entities[base_index][base_param_indexes[param_index]]):
                        for lm in syn.lemmas():
                            synonyms.append(lm.name())
                    if matched_base.entities[matched_base_index][matched_param_indexes[param_index]] not in synonyms:
                        is_match = False

                if is_match and len(base_param_indexes):
                    base.match_entities.append({
                        'matched_name': matched_base.name,
                        'matched_parameter_index': matched_base_index,
                        'my_parameter_index': base_index,
                        'my_name': base.name
                    })
