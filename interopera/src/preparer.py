from black import Line
from src.base import Base
import re
import itertools
from src.verbose import Verbose

sql_reserved_words = ['PRIMARY', 'KEY', 'UNIQUE']


class Preparer:
    def __init__(self, file_objects, approximate_all, verbose) -> None:
        self.bases = []
        self.file_objects = file_objects
        self.unique_keys = [
            line.replace('\n', '') for line in open('unique', 'r')]
        self.approximate_keys = [
            line.replace('\n', '') for line in open('approximate', 'r')]
        self.splitters = self._get_split_keys()
        self.approximate_all = approximate_all
        self.verbose = verbose

    def _get_split_keys(self):
        return [{
                'key': line.split(' ')[0],
                'splitter': line.replace('\n', '').split(' ', 1)[1]
                } for line in open('split', 'r')]

    def prepare_bases(self):
        for index, file_object in enumerate(self.file_objects):
            if self.verbose:
                print(f'Preparing file {index}')
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

        if self.verbose:
            verbose = Verbose("Reading lines", len(lines))

        for index in range(0, len(lines)):
            line = lines[index]

            if self.verbose:
                verbose.update()

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
                        'unique': parameter in self.unique_keys or not self.unique_keys,
                        'approximate': parameter in self.approximate_keys or self.approximate_all,
                        'parameter': parameter,
                        'splitters': [
                            splitter['splitter'] for splitter in self.splitters if splitter['key'] == parameter],
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
                raw_entity = []
                for words_index, word in enumerate(words):
                    splitters = parameters[words_index]['splitters']
                    splitters = list(map(lambda x: re.escape(x), splitters))
                    if splitters:
                        split_entity = "|".join(splitters)
                        raw_entity.append(
                            re.split(
                                split_entity,
                                self._preparer_strip(word)))
                    else:
                        raw_entity.append([self._preparer_strip(word)])
                entities.extend(list(itertools.product(*raw_entity)))

    def _split(self, line, splitter):
        for splitter in splitter:
            line = line.split(splitter)
        return line

    def _prepare_csv_file(self, file_object):
        lines = file_object['file'].readlines()

        parameters = []

        for parameter in lines[0].split(','):
            striped_parameter = self._preparer_strip(parameter)
            parameter_object = {
                'unique': striped_parameter in self.unique_keys or not self.unique_keys,
                'approximate': striped_parameter in self.approximate_keys or self.approximate_all,
                'parameter': striped_parameter,
                'splitters': [
                    splitter['splitter'] for splitter in self.splitters if splitter['key'] == striped_parameter],
                'type': []}

            parameters.append(parameter_object)

        entities = []

        for index, line in enumerate(lines[1:]):
            words = re.findall(
                r'(?:(?<=^)|(?<=,))(?:"(?:[^"]|"")*"|[^,])*(?:(?=$)|(?=,))', line)
            raw_entity = []

            if self.verbose:
                print(f'Reading line {index}')

            for words_index, word in enumerate(words):
                splitters = parameters[words_index]['splitters']
                splitters = list(map(lambda x: re.escape(x), splitters))
                if splitters:
                    split_entity = "|".join(splitters)
                    raw_entity.append(
                        re.split(
                            split_entity,
                            self._preparer_strip(word)))
                else:
                    raw_entity.append([self._preparer_strip(word)])
            entities.extend(list(itertools.product(*raw_entity)))
        base = Base(
            file_object['name'],
            parameters,
            entities,
            file_object['extension'],
            file_object['name'])
        self.bases.append(base)
