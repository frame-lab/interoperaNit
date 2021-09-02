import textdistance
import numpy as np

class Align:
    def __init__(self, ontos):
        self.ontos = ontos

    def _parser_input(self):
        list_classes = []
        list_properties = []
        for onto in self.ontos:
            list_classes.append(list(onto.classes()))
            list_properties.append(list(onto.object_properties()))

        list_classes_names = []
        for class_list in list_classes:
            list_name = []
            for class_object in class_list:
                list_name.append(class_object.name)
            list_classes_names.append(list_name)

        list_properties_names = []
        for property_list in list_properties:
            list_name = []
            for property_object in property_list:
                list_name.append(property_object.name)
            list_properties_names.append(list_name)

        list_input = [*np.array(np.meshgrid(list_classes_names[0], list_classes_names[1])).T.reshape(-1, 2),
                      *np.array(np.meshgrid(list_properties_names[0], list_properties_names[1])).T.reshape(-1, 2)]

        return list_input

    def make_print(self, result):
        file = open(f'./results/ontology_result.txt', "w+")
        file.writelines(str(result))

    def align(self):
        matriz_comp = self._parser_input()
        matriz_result = []
        for pair in matriz_comp:
            matriz_result.append(textdistance.hamming(pair[0], pair[1]))
        self.make_print(matriz_result)