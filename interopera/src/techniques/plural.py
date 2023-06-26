import inflect


class Plural:
    engine = inflect.engine()

    @staticmethod
    def pluralize(word: str) -> str:
        if len(word) >= 1:
            return Plural.engine.plural(word)
        return word
