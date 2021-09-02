from owlready2 import *


class Read:
    def __init__(self, ontos):
        self.ontos = ontos

    def read(self):
        for pos in range(len(self.ontos)):
            file = open(f'./results/ontology{pos}.txt', "w+")

            file.write("Classes - \n")
            list_classes = list(self.ontos[pos].classes())
            file.writelines(str(list_classes))

            file.write("\n\nIndividuals - \n")
            list_individuals = list(self.ontos[pos].individuals())
            file.writelines(str(list_individuals))

            file.write("\n\nObject properties - \n")
            list_object_properties = list(self.ontos[pos].object_properties())
            file.writelines(str(list_object_properties))

            file.write("\n\nData properties - \n")
            list_data_properties = list(self.ontos[pos].data_properties())
            file.writelines(str(list_data_properties))
            
            file.close()
