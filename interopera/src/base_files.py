from os import walk


class MultipleExtensionsException(BaseException):
    pass

class BaseFiles:
    def __init__(self, verbose) -> None:
        self.path = './samples/'
        self.verbose = verbose

    def samples(self):
        file_objects = []
        for (_, _, filenames) in walk(self.path):
            for i in range(0, len(filenames)):
                if self.verbose:
                    print(f'Reading file {filenames[i]}')
                extension_index = filenames[i].rindex('.')
                file = open(self.path + filenames[i], 'r', encoding='utf-8')
                file_object = {
                    'name': filenames[i][:extension_index],
                    'extension': filenames[i][extension_index:],
                    'file': file
                }
                file_objects.append(file_object)
        if len(file_objects) == 0:
            print('you have to put the files in the sample folder')
        return file_objects
