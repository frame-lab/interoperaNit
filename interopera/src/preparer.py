from src.base import Base

sql_reserved_words = ['PRIMARY', 'KEY', 'UNIQUE']


class Preparer:
    def __init__(self, file_objects) -> None:
        self.bases = []
        self.file_objects = file_objects
        self.unique_keys = [
            line.replace('\n', '') for line in open('unique', 'r')]

    def prepare_bases(self):
        for file_object in self.file_objects:
            if file_object['extension'] == '.sql':
                self._prepare_sql_file(file_object)
        return self.bases

    def _sql_strip(self, text):
        return text\
            .replace('\t', '')\
            .replace('"', '')\
            .replace('`', '')\
            .replace(',', '')\
            .replace('(', '')\
            .replace(')', '')\
            .replace('\n', '')\
            .replace("'", '')

    def _prepare_sql_file(self, file_object):
        new = False
        is_entities = False

        name = ''
        parameters = []
        entities = []

        lines = file_object['file'].readlines()

        for index in range(0, len(lines)):
            line = lines[index]

            if 'CREATE TABLE IF NOT EXISTS ' in line:
                words = line.split(' ')
                name = self._sql_strip(words[5])
                new = True

            elif ';' in line and new:
                new = False

            elif new:
                words = line.split(' ')
                parameter = self._sql_strip(words.pop(0))
                if parameter not in sql_reserved_words:
                    parameter_object = {
                        'unique': parameter in self.unique_keys,
                        'parameter': parameter,
                        'type': [self._sql_strip(word) for word in words]
                    }
                    parameters.append(parameter_object)
                else:
                    key = self._sql_strip(words[-1])
                    for parameter_object in parameters:
                        if parameter_object['parameter'] == key:
                            parameter_object['unique'] = True

            elif ';' in line and is_entities and \
                    f'INSERT INTO' not in lines[index + 1]:
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

            elif f'INSERT INTO' in line:
                is_entities = True

            elif is_entities:
                words = line.split(', ')
                entity = [self._sql_strip(word) for word in words]
                entities.append(entity)
