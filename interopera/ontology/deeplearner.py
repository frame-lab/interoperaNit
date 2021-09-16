import deepmatcher as dm


class Deeplearner:
    def __init__(self) -> None:
        self.model = dm.MatchingModel()
        self.paths = []

    def _parser_input(self, ontologies):
        for ontology in ontologies:
            self.paths.append(f'{ontology.domain_name}.csv')
            f = open(f'{ontology.domain_name}.csv', 'w')
            
            separator = ','
            f.write(f'{separator.join(ontology.domain_parameters)}\n')
            for entity in ontology.domain_entities:
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
        for path in self.paths:
            unlabeled = dm.data.process_unlabeled(
                path=path,
                trained_model=self.model)
            predictions = self.model.run_prediction(
                unlabeled, output_attributes=True)
            predictions.head()
