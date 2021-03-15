class IO:
    def __init__(self, file):
        self.file = file

    def write_to_file(self, data):
        with open(self.file, "a") as file:
            file.write(data + "\n")
