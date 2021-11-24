import textdistance
import copy


class Distancy:
    @staticmethod
    def distance_name(base, base_candidate):
        if textdistance.hamming.normalized_similarity(
                base.name, base_candidate.name) > 0.75 and \
                base_candidate.name not in base.match_name:
            base.match_name.append(
                base_candidate.name)

    @staticmethod
    def distance_parameter(base, base_candidate):
        for base_parameter in base.parameters:
            for base_candidate_parameter in base_candidate.parameters:
                match_parameter = {
                    'name': base_candidate.name,
                    'matched_parameter': base_candidate_parameter,
                    'my_parameter': base_parameter,
                    'approximate': base_parameter['approximate'] and base_candidate_parameter['approximate']
                }

                if base_parameter['unique'] and base_parameter['parameter'] != 'id' \
                    and textdistance.hamming.normalized_similarity(
                        base_parameter['parameter'],
                        base_candidate_parameter['parameter']) > 0.75 and \
                        match_parameter not in base.match_parameters:

                    base.match_parameters.append(match_parameter)

    @staticmethod
    def distance_entity(base, matched_base):
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

        matched_copy = copy.deepcopy(matched_base.entities)

        for base_index in range(0, len(base.entities)):
            for matched_base_index in reversed(range(0, len(matched_copy))):
                is_match = True
                for param_index in range(0, len(base_param_indexes)):
                    if textdistance.hamming.normalized_similarity(
                            base.entities[base_index][base_param_indexes[param_index]],
                            matched_base.entities[matched_base_index][matched_param_indexes[param_index]]) <= 0.75:
                        is_match = False
                
                if is_match and len(base_param_indexes):
                    base.match_entities.append({
                        'matched_name': matched_base.name,
                        'matched_parameter_index': matched_base_index,
                        'my_parameter_index': base_index,
                        'my_name': base.name
                    })
