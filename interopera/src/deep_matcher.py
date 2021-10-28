import deepmatcher as dm

class DeepMatcher:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()

    def _initialize_model(self):
        train, _, _ = dm.data.process(path='train', train='train.csv')
        self.model.initialize(train)

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

    def align(self):
        unlabeled = dm.data.process_unlabeled(
            path='csv/bigbase.csv',
            trained_model=self.model)
        predictions = self.model.run_prediction(
            unlabeled, output_attributes=True)
        predictions.head()