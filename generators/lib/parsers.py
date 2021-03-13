import re
import subprocess

import unidecode


class WordParser:
    def __init__(self, word):
        self.__word = str(word)

    @property
    def word(self):
        return self.__word

    def lowercase(self):
        self.__word = self.__word.lower()

    def remove_signs(self, order="front"):
        special = " !$@#%^&*()[]{};:,./<>?\|`~-=_+"
        for mark in special:
            if len(self.__word) == 0:
                print("dupa")
            if order == "front":
                loop = True
                tmp = self.__word
                if loop:
                    if self.__word[0] == mark:
                        self.__word = self.__word[1:]
                    else:
                        loop = False
            elif order == "reversed":
                self.__word = self.__word.rstrip("\n")
                loop = True
                tmp = self.__word
                if loop:
                    if len(self.__word) == 1:
                        if self.__word == mark:
                            self.__word == ""
                            break
                        if len(self.__word) == 0:
                            print("bbbb")
                            break
                        elif self.__word[-1] == mark:
                            self.__word = self.__word[:-1]
                    else:
                        loop = False
                self.__word = self.__word + "\n"

    def substitute_spec_signs_with_(self):
        self.__word = self.__word.translate({ord(c): "_" for c in " !$@#%^&*()[]{};:,./<>?\|`~-=_+"})

    def unidecode_polish_ltrs(self):
        self.__word = unidecode.unidecode(self.__word)

    def rip_numbers(self):
        self.__word = re.sub(r'\d+', "", self.__word)


class ListParser:
    def __init__(self, _list):
        self.__list = _list

    def remove_duplicates(self):
        self.__list = list(dict.fromkeys(self.__list))

    @property
    def list(self):
        return self.__list


class FileParser:
    def __init__(self, file):
        self.__file = file

    def sort_and_remove_duplicates(self):
        bash_command = "sort {file} | uniq >> {file}".format(file=self.__file)
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

