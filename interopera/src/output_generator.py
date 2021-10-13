import os


class OutputGenerator:
    def __init__(self, bases) -> None:
        self.bases = bases

    def generate_csv(self):
        f = open(f'csv/bigbase.csv', 'w', encoding='utf-8')

        separator = ','
        parameters = []
        entities = []

        for base in self.bases:
            empty_old_params = len(parameters) * 'None,'

            new_parameters = [f'{base.name}_{parameter_object["parameter"]}'
                              for parameter_object in base.parameters]
            parameters += new_parameters

            empty_new_params = len(new_parameters) * ',None'

            entities = [entity + empty_new_params for entity in entities]

            new_entities = [
                f'{empty_old_params}{separator.join(entity_array)}'
                for entity_array in base.entities]
            entities += new_entities

        f.write(f'{separator.join(parameters)}')
        f.writelines("%s\n" % entity for entity in entities)
