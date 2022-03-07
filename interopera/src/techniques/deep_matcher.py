import deepmatcher as dm
from random import sample
from math import ceil

class DeepMatcher:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()

    @staticmethod
    def _create_test_files(base, matched_base):
        unlabeled = open('train/unlabeled.csv', 'w', encoding='utf-8')
        train = open('train/train.csv', 'w', encoding='utf-8')
        validation = open('train/validation.csv', 'w', encoding='utf-8')
        test = open('train/test.csv', 'w', encoding='utf-8')

        parameters = ["left_" + item['my_parameter']['parameter'] for item in base.match_parameters]
        parameters += ["right_" + item['matched_parameter']['parameter'] for item in base.match_parameters]
        parameters.insert(0, 'id')

        unlabeled.write(f'{",".join(parameters)}\n')

        parameters.insert(1, 'label')

        train.write(f'{",".join(parameters)}\n')
        validation.write(f'{",".join(parameters)}\n')
        test.write(f'{",".join(parameters)}\n')

        base_index = []
        match_index = []

        for parameter in parameters[:len(parameters)//2]:
            for item in base.parameters:
                if parameter[5:] == item['parameter']:
                    base_index.append(base.parameters.index(item))

        for parameter in parameters[len(parameters)//2:]:
            for item in matched_base.parameters:
                if parameter[6:] == item['parameter']:
                    match_index.append(matched_base.parameters.index(item))

        base_matched_index_list = [i['my_parameter_index'] for i in range(len(base.match_entities))]
        matched_base_matched_index_list = [i['matched_parameter_index'] for i in range(len(base.match_entities))]

        base_list_random_indexes = sample(len(base.entities), ceil(len(base.entities) / 3))

        actual_id = 0
        actual_file = 0

        for random_index in base_list_random_indexes:

            first_entity = base.entities[random_index]

            matchs = [matched_base_matched_index_list[index] for index, i in enumerate(base_matched_index_list) if random_index == i]
            
            if matchs:
                second_entity = [matched_base.entities[matchs[0]][i] for i in match_index] 
                label = 1
            else:
                second_entity = ["null"] * len(match_index)
                label = 0

            line = [actual_id] + [first_entity[i] for i in base_index] + second_entity

            actual_id += 1

            unlabeled.write(f'{",".join(line)}\n')

            line.insert(1, label)

            if actual_file == 0:
                train.write(f'{",".join(line)}\n')
                actual_file = 1
            if actual_file == 1 or len(base_list_random_indexes) == 1:
                validation.write(f'{",".join(line)}\n')
                actual_file = 2
            if actual_file == 2 or len(base_list_random_indexes) <= 2 and actual_file == 0:
                test.write(f'{",".join(line)}\n')
                actual_file = 0
        
        matched_list_random_indexes = sample(len(matched_base.entities), ceil(len(matched_base.entities) / 3))

        first_entity = ["null"] * len(base_index)

        for random_index in matched_list_random_indexes:
            if random_index not in matched_base_matched_index_list:
                second_entity = matched_base.entities[random_index] 

                line = [actual_id] + first_entity + [second_entity[i] for i in match_index]
                
                actual_id += 1

                unlabeled.write(f'{",".join(line)}\n')

                line.insert(1, 0)

                if actual_file == 0:
                    train.write(f'{",".join(line)}\n')
                    actual_file = 1
                if actual_file == 1 or len(base_list_random_indexes) == 1:
                    validation.write(f'{",".join(line)}\n')
                    actual_file = 2
                if actual_file == 2 or len(base_list_random_indexes) <= 2 and actual_file == 0:
                    test.write(f'{",".join(line)}\n')
                    actual_file = 0

        unlabeled.close()
        train.close()
        validation.close()
        test.close()

    def _make_model(self):
        train, validation, test = dm.data.process(
            path='train',
            train='train.csv',
            validation='validation.csv',
            test='test.csv')
        self.model.run_train(
            train,
            validation,
            best_save_path='best_model.pth')
        self.model.run_eval(test)

    def align(self, base, matched_base):
        self._create_test_files(base, matched_base)
        self._make_model()
        unlabeled = dm.data.process_unlabeled(
            path='csv/bigbase.csv',
            trained_model=self.model)
        predictions = self.model.run_prediction(
            unlabeled, output_attributes=True)
        predictions.head()
        predictions.to_csv(f'results/matched.csv', index=False)