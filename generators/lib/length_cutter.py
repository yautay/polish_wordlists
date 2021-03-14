from generators.lib.generator import Generator


class LengthCutter(Generator):
    def __init__(self, minimum, maximum, **kwargs):
        super(LengthCutter, self).__init__(**kwargs)
        self.iterate_over_file(minimum, maximum)

    def iterate_over_file(self, _min, _max):
        received = 0
        processed = 0
        with open(self.file_in, "r") as _input:
            with open(self.file_out, "w") as output:
                for line in _input:
                    received += 1
                    if _min <= len(line) <= _max:
                        output.write(line + "\n")
                        processed += 1
        print("Processed {} of words in file".format(received))
        print("Omitted {} words".format(received - processed))
        print("Saved {} words in output file".format(processed))
