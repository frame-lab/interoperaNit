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
        self.match_name = []
        self.match_parameters = []
        self.file_name = file_name
