from os.path import isfile
from os import walk


class GetOntos:
    def samples(self):
        ontos = []
        path = "./samples/"
        for (_, _, filenames) in walk(path):
            for i in range(0, len(filenames)):
                onto = open(path  + filenames[i], "r")
                ontos.append(onto)
        if len(ontos) == 0:
            print("you have to put the files in the sample folder")
        return ontos
