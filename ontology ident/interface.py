from ontology.get_ontos import GetOntos
from ontology.align import Align
import sys


class OntoInterface:
    def print_help(self):
        help = open("help", "r")
        print(help.read())
        help.close()

    def align_ontology(self):
        get_ontos = GetOntos()
        ontos = get_ontos.samples()
        align_onto = Align(ontos)
        align_onto.align()


if len(sys.argv) > 1:
    face = OntoInterface()
    type = sys.argv[1]
    if type == '-h':
        face.print_help()
    elif type == '-a':
        face.align_ontology()
else:
    print("you have to pass a routine parameter")
