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

    def data(self, dataset):
        ontos = []
        path = "./data/"

        onto101 = get_ontology(path + "101_onto.rdf")
        onto101.load()
        ontos.append(onto101)

        onto = get_ontology(path + "30" + dataset + "_onto.rdf")
        onto.load()
        ontos.append(onto)

        return ontos

    def reference(self, dataset):
        path = "./data/reference-alignment/"

        ref = open(path + "30" + dataset + "_refalign.rdf", "r")
        
        return ref