from collections import namedtuple
CodeLine = namedtuple("CodeLine", ["instruction", "parameters"])
class Line():

    def __init__(self, line):
        if not isinstance(line, str):
            raise ValueError("line must be a string")
        self.line = line
    def __str__(self):
        return self.line
    def __call__(self, *args, **kwds):
        return self.line
    @property
    def is_blank(self):
        return self.line == ""
    @property
    def is_instruction(self):
        return not (self.is_blank and self.is_codeblock and self.is_comment)
    @property
    def is_codeblock(self):
        return self.line.endswith(":")
    @property
    def is_comment(self):
        return self.line.startswith("#")

class Formater():
    def validate_line(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], str):
                raise TypeError("Line must be a string")
            return func(*args, **kwargs)
        return wrapper
    @staticmethod
    @validate_line
    def format(line:str):
        line = line.upper()
        line = line.strip()
        return Line(line)
    @staticmethod
    @validate_line
    def split(line:str):
        objects = line.split()
        return CodeLine(instruction=objects[0], parameters=objects[1::])
    @validate_line
    def as_codeblock_name(line:str):
        return line.split(":")[0].strip()
    @validate_line
    def as_instruction(line:str):
        pass