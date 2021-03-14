from generators.lib.generator import Generator


class FileSplitter(Generator):
    def __init__(self, maximum: int, **kwargs):
        super(FileSplitter, self).__init__(**kwargs)
        self.__iterate_over_file(maximum)

    def __iterate_over_file(self, _max):
        _max = int(_max)
        received = 0
        processed = 0
        line_number = 0
        tmp_data = []
        batch_number = 1
        output_file = self.file_out
        with open(self.file_in, "r") as _input:
            for line in _input:
                line_number += 1
                tmp_data.append(line)
                received += 1
                if line_number == _max:
                    with open((output_file + str(batch_number)), "w") as output:
                        output.writelines(tmp_data)
                        tmp_data.clear()
                        batch_number += 1
                        line_number = 0
                        processed += 1
        print("Processed {} of words in file".format(received))
        print("Saved {} files each by {} lines".format(processed, _max))
