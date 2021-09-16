class GenerateFiles:
    def __init__(self, ontologies):
        self.ontologies = ontologies

    def make_files(self):
        for ontology in self.ontologies:
            if ontology.extension == 'sql':
                self._make_sql(ontology)

    def _make_sql(self, domain):
        file = open(f'./results/{domain.domain_name}.sql', "w+")

        file.write(
            f'CREATE TABLE IF NOT EXISTS "{domain.domain_name}" (\n')

        for parameter in domain.domain_parameters:
            separator = " "
            file.write(
                f'\t"{parameter["parameter"]}" {separator.join(parameter["type"])},\n')

        file.write(");\n\n")

        separator = ", "
        parameters = [f'"{parameter["parameter"]}"'
                      for parameter in domain.domain_parameters]
        file.write(
            f'INSERT INTO "{domain.domain_name}" ({separator.join(parameters)}) VALUES\n')

        last_entity = domain.domain_entities[-1]
        for entity in domain.domain_entities:
            file.write(
                f'\t({separator.join(entity)}),\n')

        file.write(f'\t({separator.join(last_entity)});\n')
