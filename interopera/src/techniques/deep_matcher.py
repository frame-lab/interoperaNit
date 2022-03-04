import deepmatcher as dm

class DeepMatcher:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()

    @staticmethod
    def _create_test_files(base, matched_base):
        #max cria o train csv, validation e test no caso tu vai pegar partes aleatorias de base e matched_base pra fazer os 3 arquivos.
        #Depois que conseguir criar eles, tem que adicionar mais uma coluna com o valor 0 se não foi um match na entidade e 1 se foi um match
        print('Eu sou um homem potato')

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