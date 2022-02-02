from nltk.corpus import wordnet


class Synonym:
    @staticmethod
    def synonym_comparison(first_sequence, second_sequence, type='in'):
        synonyms = []
        for syn in wordnet.synsets(first_sequence):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if type == 'in':
            return second_sequence in synonyms
        if type == 'not':
            return second_sequence not in synonyms
