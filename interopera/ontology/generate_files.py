class Ontology:
    def __init__(self, ontologies):
        self.ontologies = ontologies

    def make_files(self, domains):
        for domain in domains:
            file = open(f'./results/{domain["domain_name"]}.sql', "w+")

            file.write(
                f'CREATE TABLE IF NOT EXISTS "{domain["domain_name"]}" (\n')

            for parameter in domain["domain_parameters"]:
                separator = " "
                file.write(
                    f'\t"{parameter["parameter"]}" {separator.join(parameter["type"])},\n')

            file.write(");\n\n")

            separator = ", "
            parameters = [f'"{parameter["parameter"]}"'
                          for parameter in domain["domain_parameters"]]
            file.write(
                f'INSERT INTO "{domain["domain_name"]}" ({separator.join(parameters)}) VALUES\n')

            last_entity = domain["entities"][-1]
            for entity in domain["entities"]:
                file.write(
                    f'\t({separator.join(entity)}),\n')

            file.write(f'\t({separator.join(last_entity)});\n')
