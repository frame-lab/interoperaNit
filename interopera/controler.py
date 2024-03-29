from src.base_files import BaseFiles
from src.preparer import Preparer
from src.aligner import Aligner
from src.output_generator import OutputGenerator
from src.wordnet_check import SumoCheck
from src.sigma import Sigma
from src.consultant import Consultant
from src.validate import Validate
from dotenv import load_dotenv
import nltk
import sys


reserved = {
    '-h',
    '-s',
    '-t',
    '-e',
    '-d',
    '-m',
    '-a',
    '-v',
    '-val',
    '-max'
}

options = {
    'approximate': False,
    'synonym': False,
    'translation': False,
    'distance': False,
    'max': False,
    'verbose': False,
    'validate': False,
    'percent': 0.75,
}


class Controler:
    def print_help(self):
        help = open('help', 'r')
        print(help.read())
        help.close()

    def generate_aligner(self, verbose, validate):
        if verbose:
            print('Started the process of preparing files')
        base_files = BaseFiles(verbose)

        if validate:
            Validate.validate_csv(base_files)

        preparer = Preparer(base_files.samples(),
                            options['approximate'], verbose)
        self.aligner = Aligner(preparer.prepare_bases(), verbose)

    def align_synonym_base(self):
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        self.aligner.align_synonym_base()

    def align_translation_base(self):
        self.aligner.align_translation_base()

    def align_distance_base(self, percent):
        self.aligner.align_distance_base(percent)

    def align_exact_base(self):
        self.aligner.align_exact_base()

    def align_synonym_entities(self):
        self.aligner.align_synonym_entities()

    def align_translation_entities(self):
        self.aligner.align_translation_entities()

    def align_distance_entities(self, max, percent):
        self.aligner.align_distance_entities(max, percent)

    def align_exact_entities(self):
        self.aligner.align_exact_entities()

    def align_deep_matcher_entities(self):
        self.aligner.align_deep_matcher_entities()

    def align_magellan_entities(self):
        self.aligner.align_magellan_entities()

    def generate_outputs(self):
        output = OutputGenerator(
            self.aligner.get_aligned_bases(), options['verbose'])
        output.generate_bigbase()
        self.sumo = SumoCheck()
        output.generate_sumo_alignment(self.sumo)

    def make_sigma_inferences(self):
        self.sigma = Sigma(self.sumo.sumo_list)
        self.sigma.make_inferences()

    def run_queries(self, query):
        consultant = Consultant()
        consultant.run_queries(query)


if '-a' in sys.argv:
    options['approximate'] = True
    sys.argv.remove('-a')
if '-max' in sys.argv:
    options['max'] = True
    sys.argv.remove('-max')
if '-v' in sys.argv:
    options['verbose'] = True
    sys.argv.remove('-v')
if '-val' in sys.argv:
    options['validate'] = True
    sys.argv.remove('-val')

if options['verbose']:
    print('Process has started')

load_dotenv()
controler = Controler()
controler.generate_aligner(options['verbose'], options['validate'])

arg_len = len(sys.argv)

sys.argv.pop(0)

if '-h' in sys.argv:
    controler.print_help()
    sys.argv.remove('-h')

if options['verbose']:
    print('Starting base alignment')

if '-s' in sys.argv:
    controler.align_synonym_base()
    options['synonym'] = True
    sys.argv.remove('-s')
if '-t' in sys.argv:
    controler.align_translation_base()
    options['translation'] = True
    sys.argv.remove('-t')
if '-e' in sys.argv:
    actual_index = sys.argv.index("-e")
    if len(sys.argv) > actual_index + 1 and sys.argv[actual_index+1].isdigit():
        options['percent'] = float(sys.argv[actual_index+1]) / 100
    controler.align_distance_base(options['percent'])
    options['distance'] = True
    sys.argv.remove('-e')

if arg_len > 1:
    if options['verbose']:
        print('Starting entity alignment')

    controler.align_exact_entities()

    if options['synonym']:
        controler.align_synonym_entities()
    if options['translation']:
        controler.align_translation_entities()
    if options['distance']:
        controler.align_distance_entities(options['max'], options['percent'])
    if '-dm' in sys.argv:
        controler.align_deep_matcher_entities()
        sys.argv.remove('-d')
    if '-m' in sys.argv:
        controler.align_magellan_entities()
        sys.argv.remove('-m')

    if options['verbose']:
        print('Generating csv files')

    controler.generate_outputs()

queries = [
    line.replace('\n', '') for line in open('queries', 'r')]

if options['verbose']:
    print('Searching for queries')

controler.run_queries(queries)

if options['verbose']:
    print('Making inferences')

controler.make_sigma_inferences()

if options['verbose']:
    print('Process has ended')
