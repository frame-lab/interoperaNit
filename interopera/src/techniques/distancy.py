import textdistance


class Distancy:
    def __init__(self, percent) -> None:
        self.percent = percent

    def distancy_comparison(self, first_sequence, second_sequence, type='gt'):
        if type == 'gt':
            return textdistance.hamming.normalized_similarity(
                first_sequence, second_sequence) > self.percent
        elif type == 'le':
            return textdistance.hamming.normalized_similarity(
                first_sequence, second_sequence) <= self.percent

    def distancy_value(first_sequence, second_sequence):
        return textdistance.hamming.normalized_similarity(
            first_sequence, second_sequence)
