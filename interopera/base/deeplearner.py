import deepmatcher as dm


class Deeplearner:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()

    def _parser_input(self, bases):
        f = open(f'bigbase.csv', 'w')
        for base in bases:
            separator = ','
            f.write(f'{separator.join(base.parameters)}\n')
            for entity in base.entities:
                f.write(f'{separator.join(entity)}\n')

    def make_model(self):
        train, validation, test = dm.data.process(
            path='train',
            train='amz_goog_train.csv',
            validation='amz_goog_validation.csv',
            test='amz_goog_test.csv')
        self.model.run_train(
            train,
            validation,
            best_save_path='best_model.pth')
        self.model.run_eval(test)
        unlabeled = dm.data.process_unlabeled(
            path='train/amz_goog_unlabeled.csv',
            trained_model=self.model)
        self.model.run_prediction(unlabeled, output_attributes=True)

    def align(self):
        unlabeled = dm.data.process_unlabeled(
            path='bigbase.csv',
            trained_model=self.model)
        predictions = self.model.run_prediction(
            unlabeled, output_attributes=True)
        predictions.head()
