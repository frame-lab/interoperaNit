from src.techniques.translation import Translation

from textdistance import hamming
from csv import writer


class Word:
    def __init__(self, word, translation, phrase, word_type):
        self.word = word
        self.translation = translation
        self.syn = phrase[-1][2:-1]
        self.code = phrase[0]
        self.relation = self.get_relation(phrase)
        self.type = word_type
        self.meaning = self.get_meaning(phrase)

    @staticmethod
    def get_relation(phrase):
        relation = phrase[-1][-1]
        if relation == "=":
            return "equivalent"
        elif relation == "+":
            return "subsumed"
        else:
            return "instance"

    @staticmethod
    def get_meaning(phrase):
        start = phrase.index("|")
        meaning = ""
        for word in phrase[start+1:-1]:
            meaning += f" {word}"
        return meaning.lstrip()


class NullWord:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.syn = "null"
        self.code = "null"
        self.relation = "null"
        self.type = "null"
        self.meaning = "null"


class SumoCheck:
    def __init__(self) -> None:
        self.input_list = self.wl_create()
        self.target = "en"
        self.adj = open("wordnet/WordNetMappings30-adj.txt", 'r').readlines()[70:-1]
        self.adv = open("wordnet/WordNetMappings30-adv.txt", 'r').readlines()[70:-1]
        self.noun = open("wordnet/WordNetMappings30-noun.txt", 'r').readlines()[70:-1]
        self.verb = open("wordnet/WordNetMappings30-verb.txt", 'r').readlines()[70:-1]
        self.wordnet = {"adj": self.adj, "adv": self.adv, "noun": self.noun, "verb": self.verb}
        self.selected_words = []
        self.header = ["word", "translated_word", "code", "wordnet synonym", "relation", "file", "meaning"]
        self.data = [] 

    @staticmethod
    def wl_create() -> list:
        wl = open("csv/bigbase.csv", 'r').readlines()[0]
        wl = wl.split(",")
        for i in range(len(wl)):
            wl[i] = wl[i].split("_", maxsplit=1)[1].replace("\n", "")
        wl = sorted(list(set(wl)))

        return wl

    def get_translation(self, word) -> str:
        translation = Translation()
        return translation.translation_word(word, self.target)

    def distance_select(self, t_word, match_list):
        selected_match = 0
        selected_similarity = 0
        for match, i in zip(match_list, range(len(match_list))):
            similarity = hamming.normalized_similarity(match.syn, t_word)
            if similarity > selected_similarity:
                selected_match = i
                selected_similarity = similarity

        self.selected_words.append(match_list[selected_match])

    def wordnet_search(self):
        for word in self.input_list:
            translated_word = self.get_translation(word)
            match_list = []
            match = False
            for word_type, file in self.wordnet.items():
                for line in file:
                    phrase = str(line).split()
                    lower_phrase = str(line).lower().split()[:phrase.index("|")]
                    if translated_word.lower() in lower_phrase:
                        match_list.append(Word(word, translated_word, phrase, word_type))
                        match = True
            if match:
                self.distance_select(translated_word, match_list)
            else:
                self.selected_words.append(NullWord(word, translated_word))

        self.data = zip(list(w.word for w in self.selected_words),
                        list(w.translation for w in self.selected_words),
                        list(w.code for w in self.selected_words),
                        list(w.syn for w in self.selected_words),
                        list(w.relation for w in self.selected_words),
                        list(w.type for w in self.selected_words),
                        list(w.meaning for w in self.selected_words))
