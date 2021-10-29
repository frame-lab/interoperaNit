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


class Controler:
    def print_help(self):
        help = open('help', 'r')
        print(help.read())
        help.close()

    def generate_aligner(self):
        base_files = BaseFiles()
        preparer = Preparer(base_files.samples())
        self.aligner = Aligner(preparer.prepare_bases())

    def align_base_synonym(self):
        nltk.download('wordnet')
        self.aligner.align_synonym()

    def align_base_translation(self):
        self.aligner.align_translation()

    def align_base_distance(self):
        self.aligner.align_distance()

    def align_deep_matcher(self):
        self.aligner.align_deep_matcher()

    def align_magellan(self):
        self.aligner.align_distance_entities()

    def generate_csv(self):
        output = OutputGenerator(self.aligner.get_aligned_bases())
        output.generate_csv()

    def make_consults(self, query):
        consultant = Consultant()
        consultant.run_queries(query)


load_dotenv()
controler = Controler()
controler.generate_aligner()

arg_len = len(sys.argv)

sys.argv.pop(0)

if '-h' in sys.argv:
    controler.print_help()
    sys.argv.remove('-h')
if '-s' in sys.argv:
    controler.align_base_synonym()
    sys.argv.remove('-s')
if '-t' in sys.argv:
    controler.align_base_translation()
    sys.argv.remove('-t')
if '-e' in sys.argv:
    controler.align_base_distance()
    sys.argv.remove('-e')
if '-d' in sys.argv:
    controler.align_deep_matcher()
    sys.argv.remove('-d')
if '-m' in sys.argv:
    controler.align_magellan()
    sys.argv.remove('-m')

if arg_len > 1:
    controler.generate_csv()

queries = [
    line.replace('\n', '') for line in open('queries', 'r')]

controler.make_consults(queries)
