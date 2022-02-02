import textdistance


class Distancy:
    @staticmethod
    def distancy_comparison(first_sequence, second_sequence, type='gt'):
        if type == 'gt':
            return textdistance.hamming.normalized_similarity(
                first_sequence, second_sequence) > 0.75
        elif type == 'le':
            return textdistance.hamming.normalized_similarity(
                first_sequence, second_sequence) <= 0.75

    @staticmethod
    def distancy_value(first_sequence, second_sequence):
        return textdistance.hamming.normalized_similarity(
            first_sequence, second_sequence)
