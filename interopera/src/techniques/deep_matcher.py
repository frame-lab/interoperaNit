import deepmatcher as dm
from random import randint
from math import ceil

class DeepMatcher:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()

    @staticmethod
    def _create_test_files(base, matched_base):
        #max cria o train csv, validation e test no caso tu vai pegar partes aleatorias de base e matched_base pra fazer os 3 arquivos.
        #Depois que conseguir criar eles, tem que adicionar mais uma coluna com o valor 0 se não foi um match na entidade e 1 se foi um match
        train = open('csv/train.csv', 'w', encoding='utf-8')
        validation = open('csv/validation.csv', 'w', encoding='utf-8')
        test = open('csv/test.csv', 'w', encoding='utf-8')

        parameters = list(item['matched_parameter']['parameter'] + "_1" for item in base.match_parameters)
        parameters += list(item['my_parameter']['parameter'] + "_2" for item in base.match_parameters)

        train.write(f'{",".join(parameters)}\n')
        validation.write(f'{",".join(parameters)}\n')
        test.write(f'{",".join(parameters)}\n')

        base_index = []
        match_index = []

        for parameter in parameters[:len(parameters)//2]:
            for item in base.parameters:
                if parameter[:-2] == item['parameter']:
                    base_index.append(base.parameters.index(item))

        for parameter in parameters[len(parameters)//2:]:
            for item in matched_base.parameters:
                if parameter[:-2] == item['parameter']:
                    match_index.append(matched_base.parameters.index(item))

        matched_index_list = [i for i in range(len(base.match_entities))]

        base_list = base.entities[:]
        base_size = ceil(len(base_list) / 3)

        while base_size > 0:
            random_index = randint(0, len(base_list) - 1)

            first_entity = base_list[random_index]

            if random_index in matched_index_list:
                second_entity = matched_base.entities[random_index]
                matched_index_list.remove(random_index)
            else:
                second_entity = ["null"] * len(match_index)
            line = list(first_entity[i] for i in base_index) + list(second_entity[i] for i in match_index)
            file = randint(0, 2)
            if file == 0:
                train.write(f'{",".join(line)}\n')
            elif file == 1:
                validation.write(f'{",".join(line)}\n')
            else:
                test.write(f'{",".join(line)}\n')
            base_list.remove(base_list[random_index])
            base_size -= 1

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
        # self._make_model()
        # unlabeled = dm.data.process_unlabeled(
        #     path='csv/bigbase.csv',
        #     trained_model=self.model)
        # predictions = self.model.run_prediction(
        #     unlabeled, output_attributes=True)
        # predictions.head()
        # predictions.to_csv(f'results/matched.csv', index=False)