import os


class OutputGenerator:
    def __init__(self, bases) -> None:
        self.bases = bases

    def generate_csv(self):
        f = open(f'csv/bigbase.csv', 'w', encoding='utf-8')

        separator = ','
        parameters = []
        entities = []
        entity_matches = []

        for base in self.bases:
            empty_old_params = len(parameters) * 'None,'

            actual_entity_matches = [
                entity_match for entity_match in entity_matches if base.name == entity_match['matched_name']]

            new_parameters = [f'{base.name}_{parameter_object["parameter"]}'
                              for parameter_object in base.parameters]
            parameters += new_parameters

            empty_new_params = len(new_parameters) * ',None'

            for entity in reversed(entities):
                match = False
                multiple = False
                entity_copy = entity.copy()
                for entity_match in actual_entity_matches:
                    if entity_match['my_name'] in entity['base'] and entity_match[
                            'my_parameter_index'] in entity['index'] and not multiple:
                        entity['entity_text'] += f',{separator.join(base.entities[entity_match["matched_parameter_index"]])}'
                        match = True
                        multiple = True
                    elif entity_match['my_name'] in entity['base'] and entity_match[
                            'my_parameter_index'] in entity['index'] and multiple:
                        new_entity = entity_copy.copy()
                        new_entity['entity_text'] += f',{separator.join(base.entities[entity_match["matched_parameter_index"]])}'
                        entities.insert(entities.index(entity), new_entity)
                if not match:
                    entity['entity_text'] += empty_new_params

            new_entities = [
                {
                    'base': [
                        base.name],
                    'entity_text': f'{empty_old_params}{separator.join(base.entities[entity_index])}',
                    'index': [entity_index]} for entity_index in range(
                    0,
                    len(
                        base.entities)) if entity_index not in [
                        entity_match['matched_parameter_index'] for entity_match in actual_entity_matches]]
            entities += new_entities

            entity_matches += base.match_entities

        f.write(f'{separator.join(parameters)}\n')
        f.writelines(
            "%s\n" %
            entity['entity_text'].replace(
                'NULL',
                'None') for entity in entities)

        f.close()
