from owlready2 import get_ontology
from os import walk


class MultipleExtensionsException(BaseException):
    pass


class GetOntologies:
    def __init__(self) -> None:
        self.ontogies = []
        self.path = './samples/'

    def samples(self):
        for (_, _, filenames) in walk(self.path):
            for i in range(0, len(filenames)):
                extension = filenames[i].split('.')[-1]

                if extension == 'rdf' or extension == 'owl':
                    onto = get_ontology(self.path + filenames[i]).load()
                else:
                    onto = open(self.path + filenames[i], 'r')

                ontology = {
                    'file': onto,
                    'extension': extension
                }

                self.ontogies.append(ontology)
        if len(self.ontogies) == 0:
            print('you have to put the files in the sample folder')

    def is_same_extension(self):
        extension = self.ontogies[0]['extension']
        for ontology in self.ontogies:
            if ontology['extension'] != extension:
                raise MultipleExtensionsException(
                    'Multiple extensions were found, put only one.')
