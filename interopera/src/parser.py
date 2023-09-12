from os import walk
from ontologyinstance import OntologyInstance
from ontologyclass import OntologyClass
from techniques.plural import Plural
import re


class Parser:
    def __init__(self, path: str, verbose: bool):
        self.path = path
        self.verbose = verbose
        self.ontology_context = dict()
        self.vars = dict()
        self.terms = dict()
        self.var_count = 0
        self.language = "EnglishLanguage"

        self.class_index = {
            '1': (
                'located',
                'documentation',
                'domainSubclass'
            ),
            '2': (
                'abbreviation',
                'termFormat',
                'relatedInternalConcept'
            ),
        }

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
            ontology_inferences = []
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
                                        line_list = []
                            if parentheses == 0:
                                if is_inference:
                                    ontology_inferences.append(line_holder)
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
            self.ontology_context[sample['name']]['inferences'] = ontology_inferences

    def format_lines(self, text: str) -> tuple[list[str], list[str]]:
        strings = re.findall('("[^"]*")', text)
        new_text = text
        for string in strings:
            var = f"var{self.var_count}"
            self.var_count += 1
            new_text = new_text.replace(string, var)
            self.vars[var] = string

        return strings, new_text.split('\n')

    @staticmethod
    def format_class(text: str) -> str:
        characters = (
            ')',
            '(',
            '.',
            ',',
            ';',
        )
        new_text = text
        for char in characters:
            new_text = new_text.replace(char, '')
        return new_text

    def create_attribute(self, line_list: list, instance_dict: dict[str, OntologyInstance], class_dict: dict[str, OntologyClass]) -> None:
        class_keys = class_dict.keys()
        instance_keys = instance_dict.keys()
        attribute_key = line_list[0].replace('(', '')
        result = [re.findall("^(var[0-9]*)", line) for line in line_list]
        value = ''
        var = list()
        for element in result:
            if element:
                var.append(element)
        if len(var) > 0:
            index = self.find_index(line_list, var[0][0])
            value = self.vars[Parser.format_class(line_list[index])].replace('\n', ' ')[1:-1]
            if attribute_key == "termFormat":
                entity = line_list[2].lower()
                try:
                    self.terms[line_list[1]]
                except KeyError:
                    self.terms[line_list[1]] = dict()
                self.terms[line_list[1]][entity] = value
                value = {line_list[1]: value}
                if entity not in class_keys and Plural.pluralize(entity) not in class_keys:
                    new_class = OntologyClass(entity)
                    class_dict[entity.lower()] = new_class
            else:
                entity = line_list[1]
        else:
            if attribute_key in self.class_index['1']:
                values = line_list[-1]
                entity = line_list[1]
            else:
                if len(line_list) == 2:
                    # Criar instância
                    return
                else:
                    values = list(line_list[1]) + line_list[3:]
                    entity = line_list[2]
                    for v in values:
                        value += f"{v}, "

        new_attribute = {"value": value}
        has_found = False
        entity = entity.lower()
        if entity in class_keys:
            class_dict[entity.lower()].add_attribute(
                attribute_key, new_attribute)
            has_found = True
        elif entity in instance_keys:
            instance_dict[entity.lower()].add_attribute(
                attribute_key, new_attribute)
            has_found = True

        if not has_found:
            entity = Plural.pluralize(entity)
            if entity in class_keys:
                class_dict[entity.lower()].add_attribute(
                    attribute_key, new_attribute)
            elif entity in instance_keys:
                instance_dict[entity.lower()].add_attribute(
                    attribute_key, new_attribute)

    def create_subclass(self, line_list: list, class_dict: dict[str, OntologyClass]) -> None:
        subclass = line_list[1]
        _class = self.format_class(line_list[2])
        keys = class_dict.keys()

        if _class not in keys:
            new_class = OntologyClass(_class)
            class_dict[_class.lower()] = new_class
        if subclass not in keys:
            new_subclass = OntologyClass(subclass)
            class_dict[subclass.lower()] = new_subclass
        class_dict[subclass.lower()].add_class(_class)

    def create_instance(self, line_list: list, instance_dict: dict[str, OntologyInstance]) -> None:
        target_instance = line_list[1]
        _class = self.format_class(line_list[2])
        if target_instance not in instance_dict.keys():
            new_instance = OntologyInstance(target_instance, _class)
            instance_dict[target_instance.lower()] = new_instance
        else:
            instance_dict[target_instance.lower()].add_class(_class)

    @staticmethod
    def find_index(collection: list[str], text: str):
        for index, item in enumerate(collection):
            if text in item:
                return index

    def translate_doc(self) -> None:
        for context in self.ontology_context.values():
            for _class in context["classes"].values():
                if "documentation" in _class.attributes.keys():
                    substring = _class.attributes["documentation"]["value"]
                    while substring.count("&%") > 0:
                        index = substring.index("&%")
                        substring = substring[index + 2:]
                        variable = self.format_class(substring.split(maxsplit=1)[0])
                        try:
                            text_value = self.terms[self.language][variable.lower()]
                            _class.attributes["documentation"]["value"] = _class.attributes["documentation"]["value"].replace(f"&%{variable}", text_value)
                        except KeyError:
                            try:
                                text_value = self.terms[self.language][Plural.pluralize(variable.lower())]
                                _class.attributes["documentation"]["value"] = _class.attributes["documentation"]["value"].replace(f"&%{variable}", Plural.pluralize(text_value))
                            except KeyError:
                                pass

    def read_sentence(self, text: str) -> None:
        parenthesis_stack = []

        for index, char in enumerate(text):
            if char == '(':
                parenthesis_stack.insert(0, index)

        for parenthesis_index in parenthesis_stack:
            closing_index = parenthesis_index + text[parenthesis_index:].find(')')
            substring = text[parenthesis_index:closing_index + 1]
            var_text = f"var{self.var_count}"
            self.var_count += 1
            self.vars[var_text] = substring.replace('\n', ' ')
            text = text[:parenthesis_index] + var_text + text[closing_index + 1:]


parser = Parser('sumo/', True)
parser.make_tree()
parser.translate_doc()
