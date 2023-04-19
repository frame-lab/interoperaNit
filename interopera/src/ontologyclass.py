class OntologyClass:
    name: str
    classes: set[str]
    attributes: dict

    def __init__(self, name: str):
        self.name = name
        self.classes = set()
        self.attributes = dict()

    def add_class(self, new_class: str) -> None:
        self.classes.add(new_class)

    def add_attribute(self, key: str,  attribute: dict) -> None:
        self.attributes[key] = (attribute)

    def __str__(self):
        return f'''
            Name: {self.name},
            Classes: {self.classes},
            Attributes: {self.attributes}
        '''
