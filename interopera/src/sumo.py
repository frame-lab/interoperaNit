class Sumo:
    def __init__(
            self,
            word,
            translation,
            code,
            syn,
            relation,
            meaning) -> None:
        self.word = word
        self.translation = translation
        self.code = code
        self.syn = syn
        self.relation = relation
        self.meaning = meaning
        
    def __repr__(self):
        return 'Sumo()'

    def __str__(self):
        return f'word: {self.word} {{\n' + \
            f'  translation: {self.translation},\n' + \
            f'  code: {self.code},\n' + \
            f'  syn: {self.syn},\n' + \
            f'  relation: {self.relation}\n' + \
            f'  meaning: {self.meaning},\n' + \
            f'  }}\n'