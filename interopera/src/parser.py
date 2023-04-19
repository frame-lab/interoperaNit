from os import walk
from src.ontologyinstance import OntologyInstance
from src.ontologyclass import OntologyClass


class Parser:
    def __init__(self, path: str, verbose: bool):
        self.path = path
        self.verbose = verbose
        self.ontology_context = dict()

    def samples(self) -> list:
        file_objects = []
        for (_, _, filenames) in walk(self.path):
            for i in range(0, len(filenames)):
                if self.verbose:
                    print(f'Reading file {filenames[i]}')
                extension_index = filenames[i].rindex('.')
                file = open(self.path + filenames[i], 'r', encoding='utf-8')
                file_object = {
                    'name': filenames[i][:extension_index],
                    'extension': filenames[i][extension_index:],
                    'file': file
                }
                file_objects.append(file_object)
        return file_objects

    def make_tree(self) -> None:
        samples = self.samples()
        for sample in samples:
            parentheses = 0

            is_inference = False
            multiline_content = ''
            ontology_classes = dict()
            ontology_instances = dict()
            for line in sample['file'].readlines():
                if line[:2] != ';;':
                    parentheses += line.count('(')

                    if parentheses >= 1:
                        line_list = line.strip().split(' ')
                        first_operation = line_list[0][1:]

                        if first_operation == '=>' or first_operation == 'exists':
                            is_inference = True
                        if not is_inference:
                            if ')' not in line:
                                if multiline_content == '':
                                    multiline_content = line.strip()
                                else:
                                    multiline_content += f' {line.strip()}'
                            else:
                                if multiline_content != '':
                                    line_list = multiline_content.split(' ')
                                if first_operation == 'subclass':
                                    self.create_subclass(line_list, ontology_classes)
                                elif first_operation == 'instance':
                                    self.create_instance(line_list, ontology_instances)
                                multiline_content = ''

                    parentheses -= line.count(')')
                    if parentheses == 0:
                        is_inference = False
            self.ontology_context[sample['name']] = dict()
            self.ontology_context[sample['name']]['instances'] = ontology_instances
            self.ontology_context[sample['name']]['classes'] = ontology_classes

    @staticmethod
    def format_class(line_list: str) -> str:
        return line_list[2].replace(')', '')

    def create_subclass(self, line_list: str, class_dict: dict[str, OntologyClass]) -> None:
        subclass = line_list[1]
        _class = self.format_class(line_list)
        keys = class_dict.keys()

        if _class not in keys:
            new_class = OntologyClass(_class)
            class_dict[_class] = new_class
        if subclass not in keys:
            new_subclass = OntologyClass(subclass)
            class_dict[subclass] = new_subclass
        class_dict[subclass].add_class(_class)

    def create_instance(self, line_list: str, instance_dict: dict[str, OntologyInstance]) -> None:
        target_instance = line_list[1]
        _class = self.format_class(line_list)
        if target_instance not in instance_dict.keys():
            new_instance = OntologyInstance(target_instance, _class)
            instance_dict[target_instance] = new_instance
        else:
            instance_dict[target_instance].add_class(_class)


parser = Parser('sumo/', True)
parser.make_tree()
