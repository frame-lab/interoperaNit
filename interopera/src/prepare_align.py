from interopera.src.base import Base


class PrepareAlign:
    def __init__(self, raw_bases) -> None:
        self.raw_bases = raw_bases
        self.processed_bases = []

    def prepare_bases(self):
        for base in self.raw_bases:
            self._prepare_file(base)

    def _prepare_file(self, base):
        new = False
        new_entities = False
        is_entities = False

        name = ''
        parameters = []
        entities = []

        for line in base['file']:
            if 'CREATE TABLE IF NOT EXISTS ' in line:
                words = line.split(' ')
                name = words[5].replace('"', '')
                new = True

            elif ';' in line and new:
                new = False
                new_entities = True

            elif new:
                words = line.split(' ')
                parameter = {
                    'parameter': words.pop(0).
                    replace('\t', '').
                    replace('"', ''),
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
                    'sql')
                self.processed_bases.append(base)
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
