from owlready2 import *
import numpy as np


class TrainParser:
    def parser_input(self, ontos):
        list_classes = []
        list_properties = []
        for onto in ontos:
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

    def create_tests(self, ontos, reference):
        list_classes = []
        list_properties = []
        for onto in ontos:
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

        list_x = [*np.array(np.meshgrid(list_classes_names[0], list_classes_names[1])).T.reshape(-1, 2),
                  *np.array(np.meshgrid(list_properties_names[0], list_properties_names[1])).T.reshape(-1, 2)]

        list_refs = []
        for line in reference:
            if "entity1" in line:
                entity = line.split("#")[1].split("'")[0]
                list_refs.append([entity])
            elif "entity2" in line:
                entity = line.split("#")[1].split("'")[0]
                list_refs[-1].append(entity)
            elif "relation" in line:
                entity = line.split(">")[1].split("<")[0]
                list_refs[-1].append(entity)

        list_y = []
        for element in list_x:
            result = False
            for ref in list_refs:
                if set(element).issubset(ref) and ref[-1] == "=":
                    result = True
            list_y.append(result)

        return (list_x, list_y)
