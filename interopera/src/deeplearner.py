import deepmatcher as dm
import os

class Deeplearner:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()
        if os.path.exists('./best_model.pth'):
            self.model.load_state('best_model.pth')
        else:
            self._make_model()

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

    def _test_eval(self):
        unlabeled = dm.data.process_unlabeled(
            path='train/unlabeled.csv',
            trained_model=self.model)
        self.model.run_prediction(unlabeled, output_attributes=True)

    def _train(self):
        self._make_model()
        self._test_eval()

    def parser_input(self, bases):
        if os.path.isdir('csv'):
            pass
        else:
            os.mkdir('csv')
            
        f = open(f'csv/bigbase.csv', 'w')
        for base in bases:
            separator = ','
            parameters = [param['parameter'] for param in base.parameters]
            f.write(f'{separator.join(parameters)}\n')
            for entity in base.entities:
                f.write(f'{separator.join(entity)}\n')

    def align(self):
        unlabeled = dm.data.process_unlabeled(
            path='csv/bigbase.csv',
            trained_model=self.model)
        predictions = self.model.run_prediction(
            unlabeled, output_attributes=True)
        predictions.head()
