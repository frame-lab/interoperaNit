from os import walk
from src.node import Node


class Parser:
    def __init__(self, path: str, verbose: bool):
        self.path = path
        self.verbose = verbose
        self.nodes = dict()

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
            has_node = False
            previous_name = ''
            nodes = dict()
            for line in sample['file'].readlines():
                if line[:2] != ';;':
                    parentheses += line.count('(')
                    if '(instance' in line:
                        name = line.strip().split()[-1].replace(')', '')
                        if '?' not in name:
                            if not has_node:
                                node = Node(name, [])
                                nodes[name] = node
                                has_node = True
                                previous_name = name
                            else:
                                nodes[previous_name].childs.append(name)
                    parentheses -= line.count(')')
                    if parentheses == 0:
                        has_node = False
            self.nodes[sample['name']] = nodes


parser = Parser('sumo/', True)
parser.make_tree()
for file, nodes in parser.nodes.items():
    print(file)
    for node in nodes:
        print(f'\t{node}')
