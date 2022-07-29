from src.techniques.translation import Translation
from src.sumo import Sumo

from textdistance import hamming


class Word:
    def __init__(self, word, translation, phrase, file_number):
        self.word = word
        self.translation = translation
        self.syn = phrase[-1][2:-1]
        self.code = file_number + phrase[0]
        self.relation = self.get_relation(phrase)
        self.meaning = self.get_meaning(phrase)

    @staticmethod
    def get_relation(phrase: str) -> str:
        relation = phrase[-1][-1]
        if relation == "=":
            return "equivalent"
        elif relation == "+":
            return "subsumed"
        else:
            return "instance"

    @staticmethod
    def get_meaning(phrase: str) -> str:
        start = phrase.index("|")
        meaning = ""
        for word in phrase[start+1:-1]:
            meaning += f" {word}"
        return meaning.lstrip()

    def __str__(self) -> str:
        return f"""
            Word: {self.word}
            Translation: {self.translation}
            Synonym: {self.syn}
            Code: {self.code}
            SUMO Relation: {self.relation}
            Meaning: {self.meaning}
        """


class NullWord:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.syn = "null"
        self.code = "null"
        self.relation = "null"
        self.meaning = "null"

    def __str__(self):
        return f"""
                    Word: {self.word}
                    Translation: {self.translation}
                    Synonym: null
                    Code: null
                    SUMO Relation: null
                    Meaning: null
                """


class SumoCheck:
    def __init__(self):
        self.input_list = self.wl_create()
        self.target = "en"
        self.noun = open("wordnet/WordNetMappings30-noun.txt",
                         'r').readlines()[70:-1]
        self.verb = open("wordnet/WordNetMappings30-verb.txt",
                         'r').readlines()[70:-1]
        self.adj = open("wordnet/WordNetMappings30-adj.txt",
                        'r').readlines()[70:-1]
        self.adv = open("wordnet/WordNetMappings30-adv.txt",
                        'r').readlines()[70:-1]
        self.wordnet = {"1": self.noun, "2": self.verb,
                        "3": self.adj, "4": self.adv}
        self.selected_words = []
        self.header = ["word", "translation", "code",
                       "synonym", "relation", "meaning"]
        self.data = []

    @staticmethod
    def wl_create() -> list:
        wl = open("csv/bigbase.csv", 'r').readlines()[0]
        wl = wl.split(",")
        for i in range(len(wl)):
            wl[i] = wl[i].split("_")[-1].replace("\n", "")
        wl = sorted(list(set(wl)))

        return wl

    def get_translation(self, word: str) -> str:
        translation = Translation()
        return translation.translation_word(word, self.target)

    def distance_select(self, t_word: str, match_list: list) -> None:
        selected_match = 0
        selected_similarity = 0
        for match, i in zip(match_list, range(len(match_list))):
            similarity = hamming.normalized_similarity(match.syn, t_word)
            if similarity > selected_similarity:
                selected_match = i
                selected_similarity = similarity

        self.selected_words.append(match_list[selected_match])

    def wordnet_search(self) -> None:
        for word in self.input_list:
            if word:
                translated_word = self.get_translation(word)
                match_list = []
                match = False
                for file_number, file in self.wordnet.items():
                    for line in file:
                        phrase = str(line).split()
                        lower_phrase = str(line).lower().split()[
                            :phrase.index("|")]
                        if translated_word.lower() in lower_phrase:
                            match_list.append(
                                Word(word, translated_word, phrase, file_number))
                            match = True
                if match:
                    self.distance_select(translated_word, match_list)
                else:
                    self.selected_words.append(NullWord(word, translated_word))

        self.sumo_list = [Sumo(
            w.word, 
            w.translation, 
            w.code, 
            w.syn, 
            w.relation, 
            w.meaning) for w in self.selected_words]
