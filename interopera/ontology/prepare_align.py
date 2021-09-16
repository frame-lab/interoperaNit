from ontology.ontology import Ontology


class PrepareAlign:
    def __init__(self, raw_ontologies) -> None:
        self.raw_ontologies = raw_ontologies
        self.processed_ontologies = []

    def prepare_ontologies(self):
        for ontology in self.raw_ontologies:
            if ontology['extension'] == 'rdf' or ontology['extension'] == 'owl':
                self._prepare_owl(ontology)
            else:
                self._prepare_file(ontology)

    def _prepare_owl(self, ontology):
        for ontology_class in ontology['file'].classes():

            name = ontology_class.name
            subclasses = [
                subclass.name for subclass in ontology_class.subclasses()]

            ontology = Ontology(name, subclasses, [], [], 'owl')

            self.processed_ontologies.append(ontology)

    def _prepare_file(self, ontology):
        new_domain = False
        new_entities = False
        is_entities = False

        domain_name = ''
        domain_subclasses = []
        domain_parameters = []
        domain_entities = []

        for line in ontology:
            if 'CREATE TABLE IF NOT EXISTS ' in line:
                words = line.split(' ')
                domain_name = words[5].replace('"', '')
                new_domain = True

            elif ';' in line and new_domain:
                new_domain = False
                new_entities = True

            elif new_domain:
                words = line.split(' ')
                domain_parameter = {
                    'parameter': words.pop(0).
                    replace('\t', '').
                    replace('"', ''),
                    'type': [word.
                             replace(',', '').
                             replace('\n', '') for word in words]
                }
                domain_parameters.append(domain_parameter)

            elif ';' in line and is_entities:
                is_entities = False
                ontology = Ontology(domain_name, domain_subclasses, domain_parameters, domain_entities, 'sql')
                self.processed_ontologies.append(ontology)
                domain_name = ''
                domain_subclasses = []
                domain_parameters = []
                domain_entities = []

            elif new_entities and f'INSERT INTO "{domain_name}"' in line:
                is_entities = True
                new_entities = False

            elif is_entities:
                words = line.split(', ')
                entity = [word.
                          replace('(', '').
                          replace('\t', '').
                          replace('),\n', '').
                          replace("'", '') for word in words]
                domain_entities.append(entity)
