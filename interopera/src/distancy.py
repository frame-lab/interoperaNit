import textdistance


class Distancy:
    @staticmethod
    def distance_name(first_base, second_base):
        if textdistance.hamming.normalized_similarity(
                first_base.name,
                second_base.name) > 0.75:
            first_base.match_name.append(
                second_base.name)

    @staticmethod
    def distance_parameter(first_base, second_base):
        for first_parameter in first_base.parameters:
            for second_parameter in second_base.parameters:
                if first_parameter['parameter'] != 'id' \
                    and textdistance.hamming.normalized_similarity(
                        first_parameter['parameter'],
                        second_parameter['parameter']) > 0.75:
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })
