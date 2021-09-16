from ontology.get_ontogies import GetOntologies
from ontology.prepare_align import PrepareAlign
from ontology.aligner import Aligner
from ontology.generate_files import GenerateFiles
import nltk
import sys


class OntoInterface:
    def print_help(self):
        help = open('help', 'r')
        print(help.read())
        help.close()

    def _generate_aligner(self):
        get_ontos = GetOntologies()
        get_ontos.samples()
        get_ontos.is_same_extension()
        prepare = PrepareAlign(get_ontos.ontogies)
        prepare.prepare_ontologies()
        return Aligner(prepare.processed_ontologies)

    def align_ontology_distance(self):
        aligner = self._generate_aligner()
        aligner.align_distance()
        generator = GenerateFiles(aligner.ontologies)
        generator.make_files()

    def align_ontology_synonym(self):
        nltk.download('wordnet')
        aligner = self._generate_aligner()
        aligner.align_synonym()
        generator = GenerateFiles(aligner.ontologies)
        generator.make_files()

    def align_ontology_ident(self):
        aligner = self._generate_aligner()
        aligner.align_ident()
        generator = GenerateFiles(aligner.ontologies)
        generator.make_files()

    def align_ontology_match_entity(self):
        aligner = self._generate_aligner()
        aligner.align_match_entity()
        generator = GenerateFiles(aligner.ontologies)
        generator.make_files()

if len(sys.argv) > 1:
    face = OntoInterface()
    type = sys.argv[1]
    if type == '-h':
        face.print_help()
    elif type == '-ad':
        face.align_ontology_distance()
    elif type == '-as':
        face.align_ontology_synonym()
    elif type == '-ai':
        face.align_ontology_ident()
    elif type == '-am':
        face.align_ontology_match_entity()
else:
    print('you have to pass a routine parameter')
