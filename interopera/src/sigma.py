from py4j.java_gateway import JavaGateway


class Sigma:
    def __init__(self):
        gateway = JavaGateway()
        self.sigma_app = gateway.entry_point

    def link(self, words):
        print(self.sigma_app.getWords("Virus"))
        