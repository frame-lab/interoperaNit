from src.base_files import BaseFiles
from src.preparer import Preparer
from src.aligner import Aligner
from src.output_generator import OutputGenerator
from dotenv import load_dotenv
import nltk
import sys


class Interface:
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

    def align_base_match_entity(self):
        self.aligner.align_match_entity()

    def generate_csv(self):
        output = OutputGenerator(self.aligner.get_aligned_bases())
        output.generate_csv()

load_dotenv()
interface = Interface()
interface.generate_aligner()

if len(sys.argv) > 1:
    for pos in range(1, len(sys.argv)):
        type = sys.argv[pos]
        if type == '-h':
            interface.print_help()
        elif type == '-s':
            interface.align_base_synonym()
        elif type == '-t':
            interface.align_base_translation()
        elif type == '-d':
            interface.align_base_distance()
        elif type == '-m':
            interface.align_base_match_entity()

interface.generate_csv()