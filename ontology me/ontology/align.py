import numpy as np
import deepmatcher as dm


class Align:
    def __init__(self, ontos):
        self.ontos = ontos
        self.model = dm.MatchingModel()

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

        list_input = [*np.array(np.meshgrid(list_classes_names[0],
                                            list_classes_names[1])).T.reshape(-1,
                                                                              2),
                      *np.array(np.meshgrid(list_properties_names[0],
                                            list_properties_names[1])).T.reshape(-1,
                                                                                 2)]

        return list_input

    def make_model(self):
        train, validation, test = dm.data.process(
            path='samples',
            train='train.csv',
            validation='validation.csv',
            test='test.csv')
        self.model.run_train(
            train,
            validation,
            best_save_path='best_model.pth')
        self.model.run_eval(test)

    def make_print(self, result):
        file = open(f'./results/ontology_result.txt', "w+")
        file.writelines(str(result))

    def align(self):
        unlabeled = dm.data.process_unlabeled(
            path='sample_data/itunes-amazon/unlabeled.csv',
            trained_model=self.model)
        predictions = self.model.run_prediction(unlabeled, output_attributes=True)
        predictions.head()
