from generators.lib.generator import Generator


class HashSplitter(Generator):
    def __init__(self, separator: str, **kwargs):
        super(HashSplitter, self).__init__(**kwargs)
        print("Splitting hashes to passwords")
        if separator is None:
            separator = ":"
        self.__separator = separator
        self.__parse_file()

    def __parse_file(self):
        count = 0
        with open(self.file_in, "r") as _input:
            with open(self.file_out, "w") as output:
                for line in _input:
                    password = line.split(sep=self.__separator)
                    if len(password) > 1:
                        output.write(password[-1])
                    else:
                        output.write(password[0])
                    count += 1
        print("Processed {count} passwords".format(count=count))
