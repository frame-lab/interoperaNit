class Base:
    def __init__(
            self,
            name,
            parameters,
            entities,
            extension) -> None:
        self.name = name
        self.parameters = parameters
        self.entities = entities
        self.extension = extension
        self.match_name = []
        self.match_parameters = []
