from re import fullmatch, findall
import sys


class Validate:
    @staticmethod
    def validate_csv(base_file):
        errors = []
        for sample in base_file.samples():
            name = sample['name']
            file = sample['file']
            parameters = file.readline()

            parameter_columns = findall(
                r'(?:(?<=^)|(?<=,))(?:(?:"(?:[^"]*|[^"]*"+[^"]+"*|[^"]*"{2,})")|(?:"[^,]*"[^,]*[^",])|[^",][^,]*)(?:(?=$)|(?=,))', parameters)
            parameter_column_text = ''.join(parameter_columns)
            parameter_column_count = 1 + parameters.count(',') - parameter_column_text.count(',') 

            for index, line in enumerate(file.readlines()):
                match = fullmatch(r'((("([^"]*|[^"]*"+[^"]+"*|[^"]*"{2,})")|("[^,]*"[^,]*[^",])|[^",][^,]*),*)*', line)
                if not match:
                    line_quotes = line.count('"')
                    if line_quotes > 0:
                        error = f'\nAn error of quotes was found in the line {index} of the file {name}'
                        errors.append(error)

                line_columns = findall(r'(?:(?<=^)|(?<=,))(?:(?:"(?:[^"]*|[^"]*"+[^"]+"*|[^"]*"{2,})")|(?:"[^,]*"[^,]*[^",])|[^",][^,]*)(?:(?=$)|(?=,))', line)
                line_columns_text = ''.join(line_columns)
                line_column_count = 1 + line.count(',') - line_columns_text.count(',') 

                if line_column_count != parameter_column_count and match:
                    error = f'\nAn error of column was found in the line {index} of the file {name}: ' \
                            f'Number of columns is {line_column_count} when it should be {parameter_column_count}.'
                    errors.append(error)
        if errors:
            error_text = ' '.join(errors)
            sys.exit(error_text)
