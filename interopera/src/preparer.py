from src.base import Base


class Preparer:
    def __init__(self, file_objects) -> None:
        self.bases = []
        self.file_objects = file_objects
        self.unique_keys = [
            line.replace('\n', '') for line in open('unique', 'r')]

    def prepare_bases(self):
        for file_object in self.file_objects:
            self._prepare_file(file_object)
        return self.bases

    def _prepare_file(self, file_object):
        new = False
        new_entities = False
        is_entities = False

        name = ''
        parameters = []
        entities = []

        for line in file_object['file']:
            if 'CREATE TABLE IF NOT EXISTS ' in line:
                words = line.split(' ')
                name = words[5].replace('"', '')
                new = True

            elif ';' in line and new:
                new = False
                new_entities = True

            elif new:
                words = line.split(' ')
                parameter = words.pop(0).replace('\t', '').replace('"', '')
                parameter = {
                    'unique': parameter in self.unique_keys,
                    'parameter':parameter,
                    'type': [word.
                             replace(',', '').
                             replace('\n', '') for word in words]
                }
                parameters.append(parameter)

            elif ';' in line and is_entities:
                is_entities = False
                base = Base(
                    name,
                    parameters,
                    entities,
                    file_object['extension'],
                    file_object['name'])
                self.bases.append(base)
                name = ''
                parameters = []
                entities = []

            elif new_entities and f'INSERT INTO "{name}"' in line:
                is_entities = True
                new_entities = False

            elif is_entities:
                words = line.split(', ')
                entity = [word.
                          replace('(', '').
                          replace('\t', '').
                          replace('),\n', '').
                          replace("'", '') for word in words]
                entities.append(entity)
