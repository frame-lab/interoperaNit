from src.base_files import BaseFiles
from src.preparer import Preparer
from src.aligner import Aligner
from src.output_generator import OutputGenerator
from src.consultant import Consultant
from dotenv import load_dotenv
import nltk
import sys


reserved = {
    '-h',
    '-s',
    '-t',
    '-e',
    '-d',
    '-m'
}

options = {
    'approximate': False,
    'synonym': False,
    'translation': False,
    'distance': False,
}


class Controler:
    def print_help(self):
        help = open('help', 'r')
        print(help.read())
        help.close()

    def generate_aligner(self):
        base_files = BaseFiles()
        preparer = Preparer(base_files.samples())
        self.aligner = Aligner(preparer.prepare_bases())

    def align_synonym_base(self):
        nltk.download('wordnet')
        self.aligner.align_synonym_base()

    def align_translation_base(self):
        self.aligner.align_translation_base()

    def align_distance_base(self):
        self.aligner.align_distance_base()

    def align_exact_base(self):
        self.aligner.align_exact_base()

    def align_synonym_entities(self):
        self.aligner.align_synonym_entities()

    def align_translation_entities(self):
        self.aligner.align_translation_entities()

    def align_distance_entities(self):
        self.aligner.align_distance_entities()

    def align_exact_entities(self):
        self.aligner.align_exact_entities()

    def align_deep_matcher_entities(self):
        self.aligner.align_deep_matcher_entities()

    def align_magellan_entities(self):
        self.aligner.align_magellan_entities()

    def generate_csv(self):
        output = OutputGenerator(self.aligner.get_aligned_bases())
        output.generate_csv()

    def run_queries(self, query):
        consultant = Consultant()
        consultant.run_queries(query)


load_dotenv()
controler = Controler()
controler.generate_aligner()

arg_len = len(sys.argv)

sys.argv.pop(0)

if '-a' in sys.argv:
    options['approximate'] = True
    sys.argv.remove('-a')

if '-h' in sys.argv:
    controler.print_help()
    sys.argv.remove('-h')

if '-s' in sys.argv:
    controler.align_synonym_base()
    sys.argv.remove('-s')
if '-t' in sys.argv:
    controler.align_translation_base()
    sys.argv.remove('-t')
if '-e' in sys.argv:
    controler.align_distance_base()
    sys.argv.remove('-e')

if arg_len > 1:
    if '-d' in sys.argv:
        # controler.align_deep_matcher_entities()
        sys.argv.remove('-d')
    if '-m' in sys.argv:
        # controler.align_magellan_entities()
        sys.argv.remove('-m')
    if not options['approximate']:
        controler.align_exact_entities()
    else:
        if options['synonym']:
            controler.align_synonym_entities()
        if options['translation']:
            controler.align_translation_entities()
        if options['distance']:
            controler.align_distance_entities()
    controler.generate_csv()

queries = [
    line.replace('\n', '') for line in open('queries', 'r')]

controler.run_queries(queries)
