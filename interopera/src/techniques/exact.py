class Exact:
    @staticmethod
    def exact_comparison(first_sequence, second_sequence, type='eq'):
        if type == 'eq':
            return first_sequence == second_sequence
        elif type == 'ne':
            return first_sequence != second_sequence
