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

        for i in range(0, len(domain.domain_parameters)):
            parameter = domain.domain_parameters[i]
            separator = " "
            if i < len(domain.domain_parameters) - \
                    1 or domain.match_parameters:
                file.write(
                    f'\t"{parameter["parameter"]}" {separator.join(parameter["type"])},\n')
            else:
                file.write(
                    f'\t"{parameter["parameter"]}" {separator.join(parameter["type"])}\n')

        for i in range(0, len(domain.match_parameters)):
            match = domain.match_parameters[i]
            if i < len(domain.match_parameters) - 1:
                file.write(
                    f'\t"{match["domain_name"]}_id" BIGINT NULL DEFAULT NULL,\n')
            else:
                file.write(
                    f'\t"{match["domain_name"]}_id" BIGINT NULL DEFAULT NULL\n')

        file.write(");\n\n")

        separator = ", "
        parameters = [f'"{parameter["parameter"]}"'
                      for parameter in domain.domain_parameters]

        for match in domain.match_parameters:
            parameters.append(f'"{match["domain_name"]}_id"')

        file.write(
            f'INSERT INTO "{domain.domain_name}" ({separator.join(parameters)}) VALUES\n')

        for i in range(0, len(domain.domain_entities)):
            entity = domain.domain_entities[i]
            for match in domain.match_parameters:
                entity.append('NULL')
            if i < len(domain.domain_entities) - 1:
                file.write(
                    f'\t({separator.join(entity)}),\n')
            else:
                file.write(
                    f'\t({separator.join(entity)});\n')
