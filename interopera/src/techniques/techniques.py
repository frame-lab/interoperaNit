import copy


class Techniques:
    @staticmethod
    def techniques_name(base, base_candidate, technique):
        if technique(base.name, base_candidate.name) and \
           base_candidate.name not in base.match_name:
            base.match_name.append(
                base_candidate.name)

    @staticmethod
    def techniques_parameter(base, base_candidate, technique):
        for base_parameter in base.parameters:
            for base_candidate_parameter in base_candidate.parameters:
                match_parameter = {
                    'name': base_candidate.name,
                    'matched_parameter': base_candidate_parameter,
                    'my_parameter': base_parameter,
                    'approximate': base_parameter['approximate'] and base_candidate_parameter['approximate']}

                if base_parameter['unique'] and \
                   base_parameter['parameter'] != 'id' and \
                   technique(
                        base_parameter['parameter'],
                        base_candidate_parameter['parameter']) and \
                        match_parameter not in base.match_parameters:
                    base.match_parameters.append(match_parameter)

    @staticmethod
    def techniques_entity(base, matched_base, technique, comparison_type, should_approximate):
        if should_approximate:
            match_params = [parameter for parameter in base.match_parameters
                            if parameter['name'] == matched_base.name and parameter['approximate']]
        else:
            match_params = [parameter for parameter in base.match_parameters
                if parameter['name'] == matched_base.name and not parameter['approximate']]

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
                    if technique(base.entities[base_index][base_param_indexes[param_index]],
                                 matched_base.entities[matched_base_index][matched_param_indexes[param_index]],
                                 comparison_type):
                        is_match = False

                if is_match and len(base_param_indexes):
                    base.match_entities.append({
                        'matched_name': matched_base.name,
                        'matched_parameter_index': matched_base_index,
                        'my_parameter_index': base_index,
                        'my_name': base.name
                    })

    @staticmethod
    def techniques_entity_max(base, matched_base, technique):
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
            percent = 0
            target_object = {}
            for matched_base_index in reversed(range(0, len(matched_copy))):
                target_percent = 0
                for param_index in range(0, len(base_param_indexes)):
                    target_percent += technique(base.entities[base_index][base_param_indexes[param_index]],
                                                matched_base.entities[matched_base_index][matched_param_indexes[param_index]])
                if target_percent > percent and len(base_param_indexes):
                    percent = target_percent
                    target_object = {
                        'matched_name': matched_base.name,
                        'matched_parameter_index': matched_base_index,
                        'my_parameter_index': base_index,
                        'my_name': base.name
                    }
            if target_object:
                base.match_entities.append(target_object)
