from re import match, findall


class FormatCsvException(Exception):
    pass


class Validate:
    @staticmethod
    def validate_csv(base_file):
        for sample in base_file.samples():
            name = sample['name']
            file = sample['file']
            columns = len(findall(r'(?:(?<=^)|(?<=,))(?:"(?:[^"]|"")*"|[^,])*(?:(?=$)|(?=,))', file.readline()))

            for index, line in enumerate(file.readlines()[1:]):
                if not match(r'(("([^"]|"")"|[^,])*,*)*', line):
                    line_columns = len(findall(r'(?:(?<=^)|(?<=,))(?:"(?:[^"]|"")*"|[^,])*(?:(?=$)|(?=,))', line))
                    line_quotes = line.count('"')
                    if line_columns != columns:
                        error = f'An error of column was found in the line {index} of the file {name}:\n' \
                                f'Number of columns is {line_columns} when it should be {columns}.'
                    elif line_quotes % 2 == 1:
                        error = f'An error of quote was found in the line {index} of the file {name}:\n' \
                                f'Number of quotes is odd ({line_quotes}).'
                    else:
                        error = 'Unknown error.'
                    raise FormatCsvException(error)

