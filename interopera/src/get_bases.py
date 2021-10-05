from os import walk


class MultipleExtensionsException(BaseException):
    pass


class GetBases:
    def __init__(self) -> None:
        self.bases = []
        self.path = './samples/'

    def samples(self):
        for (_, _, filenames) in walk(self.path):
            for i in range(0, len(filenames)):
                extension = filenames[i].split('.')[-1]
                base = open(self.path + filenames[i], 'r')
                base = {
                    'file': base,
                    'extension': extension
                }
                self.bases.append(base)
        if len(self.bases) == 0:
            print('you have to put the files in the sample folder')
