from owlready2 import get_ontology
from os.path import isfile
import sys

class GetOntos:
    def samples(self):
        ontos = []
        path = "./samples/"
        for pos in sys.argv:
            arg = pos
            if isfile(path + arg):
                onto = get_ontology(path + arg)
                onto.load()
                ontos.append(onto)
        if len(ontos) == 0:
            print("you have to pass a path to the files")
        return ontos