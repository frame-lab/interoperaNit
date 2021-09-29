from base.get_bases import GetBases
from base.prepare_align import PrepareAlign
from base.aligner import Aligner
from dotenv import load_dotenv
import nltk
import sys


class Interface:
    def print_help(self):
        help = open('help', 'r')
        print(help.read())
        help.close()

    def generate_aligner(self):
        get_bases = GetBases()
        get_bases.samples()
        prepare = PrepareAlign(get_bases.bases)
        prepare.prepare_bases()
        return Aligner(prepare.processed_bases)

    def align_base_synonym(self, aligner):
        nltk.download('wordnet')
        aligner.align_synonym()

    def align_base_translation(self, aligner):
        aligner.align_translation()

    def align_base_distance(self, aligner):
        aligner.align_distance()

    def align_base_match_entity(self, aligner):
        aligner.align_match_entity()


load_dotenv()
interface = Interface()
aligner = interface.generate_aligner()

if len(sys.argv) > 1:
    for pos in range(1, len(sys.argv)):
        type = sys.argv[pos]
        if type == '-h':
            interface.print_help()
        elif type == '-s':
            interface.align_base_synonym(aligner)
        elif type == '-t':
            interface.align_base_translation(aligner)
        elif type == '-d':
            interface.align_base_distance(aligner)

interface.align_base_match_entity(aligner)
