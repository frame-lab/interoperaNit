from ia.train_parser import TrainParser
from ia.machine_learning import learn
from ontology.get_ontos import GetOntos
from ontology.align import Align
from ontology.read import Read
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

    def read_ontology(self):
        get_ontos = GetOntos()
        ontos = get_ontos.samples()
        read_onto = Read(ontos)
        read_onto.read()
    
    def train_ml(self):
        dataset = sys.argv[2]
        
        get_ontos = GetOntos()
        ontos = get_ontos.data(dataset)
        reference = get_ontos.reference(dataset)

        train_parser = TrainParser()
        list_x, list_y = train_parser.create_tests(ontos, reference)
        ml = learn()
        processed_x, processed_y = ml.train_preprocessor(list_x, list_y)
        ml.test_split(processed_x, processed_y)
        ml.train_ia()
        ml.predict_test()
        ml.save_model()

if len(sys.argv) > 1:
    face = OntoInterface()
    type = sys.argv[1]
    if type == '-h':
        face.print_help()
    elif type == '-r':
        face.read_ontology()
    elif type == '-a':
        face.align_ontology()
    elif type == '-t':
        face.train_ml()
else:
    print("you have to pass a routine parameter")
