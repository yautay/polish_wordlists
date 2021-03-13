class Generator:
    def __init__(self, **kwargs):
        if "file_in" in kwargs:
            print("Input file: {}".format(kwargs["file_in"]))
            self.file_in = kwargs["file_in"]
        else:
            self.file_in = None
        if "file_out" in kwargs:
            print("Output file: {}".format(kwargs["file_out"]))
            self.file_out = kwargs["file_out"]
        else:
            self.file_out = None

    @staticmethod
    def count_lines(file):
        lines = 0
        with open(file, "r") as data:
            for line in data:
                lines += 1
        return lines
