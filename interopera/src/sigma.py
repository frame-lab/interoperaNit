from py4j.java_gateway import JavaGateway


class Sigma:
    def __init__(self, sumo_list):
        gateway = JavaGateway()
        self.sigma_app = gateway.entry_point
        self.sumo_list = sumo_list
        self.inferences = [
            line.replace('\n', '') for line in open('inferences', 'r')]

    def make_inferences(self):
        for inference in self.inferences:
            data_replace = [data for data in self.sumo_list if data.word in inference]
            if data_replace:
                for data in data_replace:
                    inference.replace(data.word, data.translation)
            print(self.sigma_app.getWords(inference))

    def make_formula(self, formula, args):
        self.sigma_app.query(formula, args, term)

    def get_words(self, term):
        self.sigma_app.getWords(term)