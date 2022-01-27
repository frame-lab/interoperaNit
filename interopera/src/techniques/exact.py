class Exact:
    @staticmethod
    def exact_name(base_name, base_candidate_name):
        return base_name == base_candidate_name

    @staticmethod
    def exact_parameter(base_parameter, base_candidate_parameter):
        return base_parameter == base_candidate_parameter

    @staticmethod
    def exact_entity(base_entity, matched_base_entity):
        return base_entity != matched_base_entity
