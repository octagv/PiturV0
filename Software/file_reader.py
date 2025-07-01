class FileReader():
    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("filename must be a string")
        self.__file = open(filename, "r")
    def iter_line(self):
        for line in self.__file:
            yield line
    def __del__(self):
        self.__file.close()
