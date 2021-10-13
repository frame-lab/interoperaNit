from nltk.corpus import wordnet


class Synonym:
    @staticmethod
    def synonym_name(first_base, second_base):
        synonyms = []
        for syn in wordnet.synsets(first_base.name):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        if second_base.name in synonyms:
            first_base.match_name.append(
                second_base.name)

    @staticmethod
    def synonym_parameter(first_base, second_base):
        for first_parameter in first_base.parameters:
            synonyms = []
            for syn in wordnet.synsets(first_parameter['parameter']):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
            for second_parameter in second_base.parameters:
                if second_parameter['parameter'] in synonyms \
                        and first_parameter['parameter'] != 'id':
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })
