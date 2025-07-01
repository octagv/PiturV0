from collections import namedtuple
CodeLine = namedtuple("CodeLine", ["instruction", "parameters"])
class Formater():
    @staticmethod
    def format(line):
        if not isinstance(line, str):
            raise TypeError("Line must be a string")
        line = line.upper()
        line = line.strip()
        return line
    @staticmethod
    def split(line):
        if not isinstance(line, str):
            raise TypeError("Line must be a string")
        objects = line.split()
        return CodeLine(instruction=objects[0], parameters=objects[1::])