import textdistance


class Distancy:
    @staticmethod
    def distance_name(base_name, base_candidate_name):
        return textdistance.hamming.normalized_similarity(
            base_name, base_candidate_name) > 0.75

    @staticmethod
    def distance_parameter(base_parameter, base_candidate_parameter):
        return textdistance.hamming.normalized_similarity(
            base_parameter,
            base_candidate_parameter) > 0.75

    @staticmethod
    def distance_entity(base_entity, matched_base_entity):
        return textdistance.hamming.normalized_similarity(
            base_entity, matched_base_entity) <= 0.75
