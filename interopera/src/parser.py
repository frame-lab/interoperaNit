from os import walk
from ontologyinstance import OntologyInstance
from ontologyclass import OntologyClass
import re


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

            ontology_classes = dict()
            ontology_instances = dict()
            is_inference = False
            parentheses = 0
            line_holder = ''
            blank_line = True
            for line in sample['file'].readlines():
                if len(line.strip()) == 0 or line[0] == ';':
                    if not blank_line:
                        _, lines = self.format_lines(line_holder.rstrip())
                        multiline_content = ''
                        line_list = list()
                        for string in lines:
                            parentheses += string.count("(")
                            if parentheses >= 1:
                                line_list = [*line_list, *string.strip().split(' ')]
                                first_operation = line_list[0][1:]

                                if first_operation == "=>" or first_operation == "exists" or first_operation == "<=>":
                                    is_inference = True
                                parentheses -= string.count(')')

                                if not is_inference and parentheses == 0:
                                    if ')' not in string:
                                        if multiline_content == '':
                                            multiline_content = string.strip()
                                        else:
                                            multiline_content += f" {string.strip()}"
                                    else:
                                        if multiline_content != '':
                                            line_list = multiline_content.split(' ')
                                        if first_operation == "subclass":
                                            self.create_subclass(
                                                line_list, ontology_classes)
                                        elif first_operation == "instance":
                                            self.create_instance(
                                                line_list, ontology_instances)
                                        else:
                                            self.create_attribute(
                                                line_list, ontology_instances, ontology_classes)
                                        multiline_content = ''
                            if parentheses == 0:
                                is_inference = False
                        line_holder = ''
                    blank_line = True
                else:
                    line_holder += line.strip() + '\n'
                    blank_line = False
            self.ontology_context[sample['name']] = dict()
            self.ontology_context[sample['name']
                                  ]['instances'] = ontology_instances
            self.ontology_context[sample['name']]['classes'] = ontology_classes

    @staticmethod
    def format_lines(text: str) -> tuple[list[str], list[str]]:
        strings = re.findall('("[^"]*")', text)
        new_text = text
        for count, string in enumerate(strings):
            new_text = new_text.replace(string, f"var{count}")

        return strings, new_text.split('\n')

    @staticmethod
    def format_class(line_list: list) -> str:
        return line_list[2].replace(')', '')

    def create_attribute(self, line_list: list, instance_dict: dict[str, OntologyInstance], class_dict: dict[str, OntologyClass]) -> None:
        attribute_key = line_list[0]
        var = [re.findall("(var[0-9]*)", line) for line in line_list]
        if len(var) > 0:
            value = line_list[1]
            entity = line_list[-1]
        else:
            value = line_list[-1]
            entity = line_list[1]

        new_attribute = {"value": value, "options": line_list[1:-2]}

        class_keys = class_dict.keys()
        instance_keys = instance_dict.keys()
        if entity in class_keys:
            class_dict[entity].add_attribute(
                attribute_key.replace('(', ''), new_attribute)
        elif entity in instance_keys:
            instance_dict[entity].add_attribute(
                attribute_key.replace('(', ''), new_attribute)

    def create_subclass(self, line_list: list, class_dict: dict[str, OntologyClass]) -> None:
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

    def create_instance(self, line_list: list, instance_dict: dict[str, OntologyInstance]) -> None:
        target_instance = line_list[1]
        _class = self.format_class(line_list)
        if target_instance not in instance_dict.keys():
            new_instance = OntologyInstance(target_instance, _class)
            instance_dict[target_instance] = new_instance
        else:
            instance_dict[target_instance].add_class(_class)


parser = Parser('../sumo/', True)
parser.make_tree()
# for file, context in parser.ontology_context.items():
#     print(file)
#     for category, items in context.items():
#         print(f'\t{category}\n')
#         for key, value in items.items():
#             print(f'{key}:\n{value}')
