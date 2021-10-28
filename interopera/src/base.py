class Base:
    def __init__(
            self,
            name,
            parameters,
            entities,
            extension,
            file_name) -> None:
        self.name = name
        self.parameters = parameters
        self.entities = entities
        self.extension = extension
        self.file_name = file_name
        self.match_name = []
        self.match_parameters = []
        self.match_entities = []

    def __repr__(self):
        return 'Base()'

    def __str__(self):
        return f'name: {self.name} {{\n' + \
            f'  parameters: {self.parameters},\n' + \
            f'  entities: {self.entities},\n' + \
            f'  extension: {self.extension},\n' + \
            f'  file_name: {self.file_name}\n' + \
            f'  match_name: {self.match_name},\n' + \
            f'  match_parameters: {self.match_parameters},\n' + \
            f'  match_entities: {self.match_entities},\n' + \
            f'  }}\n'
