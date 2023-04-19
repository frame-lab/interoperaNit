class OntologyInstance:
    name: str
    classes: set[str]
    attributes: dict

    def __init__(self, name: str, _class: str):
        self.name = name
        self.classes = {_class}
        self.attributes = dict()

    def add_class(self, name: str) -> None:
        self.classes.add(name)

    def __str__(self):
        return f'''
            Name: {self.name},
            Classes: {self.classes},
            Attributes: {self.attributes} 
        '''
