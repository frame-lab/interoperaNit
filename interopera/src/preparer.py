from src.base import Base

sql_reserved_words = ['PRIMARY', 'KEY', 'UNIQUE']


class Preparer:
    def __init__(self, file_objects, approximate_all) -> None:
        self.bases = []
        self.file_objects = file_objects
        self.unique_keys = [
            line.replace('\n', '') for line in open('unique', 'r')]
        self.approximate_keys = [
            line.replace('\n', '') for line in open('approximate', 'r')]
        self.approximate_all = approximate_all

    def prepare_bases(self):
        for file_object in self.file_objects:
            if file_object['extension'] == '.sql':
                self._prepare_sql_file(file_object)
            elif file_object['extension'] == '.csv':
                self._prepare_csv_file(file_object)
            file_object['file'].close()
        return self.bases

    def _preparer_strip(self, text):
        return text\
            .replace('\t', '')\
            .replace('"', '')\
            .replace('`', '')\
            .replace(',', '')\
            .replace('(', '')\
            .replace(')', '')\
            .replace('\n', '')\
            .replace("'", '')\
            .replace(";", '')

    def _prepare_sql_file(self, file_object):
        new = False
        is_entities = False

        name = ''
        parameters = []
        entities = []

        lines = file_object['file'].readlines()

        for index in range(0, len(lines)):
            line = lines[index]

            if index == len(lines) - 1:
                is_entities = False
                words = line.split('	')
                if len(words) == 1:
                    words = line.split(', ')
                entity = [self._preparer_strip(word) for word in words]
                entities.append(entity)
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

            elif 'CREATE TABLE IF NOT EXISTS ' in line:
                words = line.split(' ')
                name = self._preparer_strip(words[5])
                new = True

            elif 'CREATE TABLE ' in line:
                words = line.split(' ')[2].split('.')[1]
                name = self._preparer_strip(words)
                new = True

            elif ';' in line and new:
                new = False

            elif new:
                words = line.strip().split(' ')
                parameter = self._preparer_strip(words.pop(0))
                if parameter not in sql_reserved_words:
                    parameter_object = {
                        'unique': parameter in self.unique_keys,
                        'approximate': parameter in self.approximate_keys or self.approximate_all,
                        'parameter': parameter,
                        'type': [
                            self._preparer_strip(word) for word in words]}
                    parameters.append(parameter_object)
                else:
                    key = self._preparer_strip(words[-1])
                    for parameter_object in parameters:
                        if parameter_object['parameter'] == key:
                            parameter_object['unique'] = True

            elif is_entities and (';' in line or line == '\\.') and \
                    f'INSERT INTO' not in lines[index + 1]:
                is_entities = False
                words = line.split(', ')
                entity = [self._preparer_strip(word) for word in words]
                entities.append(entity)
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

            elif f'COPY ' in line:
                is_entities = True

            elif is_entities:
                words = line.split('	')
                if len(words) == 1:
                    words = line.split(', ')
                entity = [self._preparer_strip(word) for word in words]
                entities.append(entity)

    def _prepare_csv_file(self, file_object):
        lines = file_object['file'].readlines()

        parameters = []

        for parameter in lines[0].split(','):
            striped_parameter = self._preparer_strip(parameter)
            parameter_object = {
                'unique': striped_parameter in self.unique_keys,
                'approximate': striped_parameter in self.approximate_keys or self.approximate_all,
                'parameter': striped_parameter,
                'type': []
            }

            parameters.append(parameter_object)

        entities = []

        for index in range(1, len(lines)):
            line = lines[index]
            if "\"" in line:
                colon_word_index = [
                    pos for pos, char in enumerate(line) if char == "\""]
                line_copy = line[colon_word_index[1]:] + self._preparer_strip(
                    line[colon_word_index[0]:colon_word_index[1]]) + line[colon_word_index[1]:]
                words = line.split(',')
            else:
                words = line.split(',')
            entity = [self._preparer_strip(word) for word in words]
            entities.append(entity)

        base = Base(
            file_object['name'],
            parameters,
            entities,
            file_object['extension'],
            file_object['name'])
        self.bases.append(base)
