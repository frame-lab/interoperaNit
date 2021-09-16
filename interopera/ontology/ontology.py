class Ontology:
    def __init__(
            self,
            domain_name,
            domain_subclasses,
            domain_parameters,
            domain_entities,
            extension) -> None:
        self.domain_name = domain_name
        self.domain_subclasses = domain_subclasses
        self.domain_parameters = domain_parameters
        self.domain_entities = domain_entities
        self.extension = extension
        self.match_name = []
        self.match_subclasses = []
        self.match_parameters = []
