from typing import Optional
class CodeBlock():
    name:str
    initial_address:int
    lines:list[str]

    def __init__(self, name, initial_address):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(initial_address, int):
            raise ValueError("actual_name must be a integer")
        self.name = name
        self.initial_address = initial_address
        self.lines = []
    def add_line(self, line):
        if not isinstance(line, str):
            raise ValueError("line must be a string")
        self.lines.append(line)

class CodeBlockController():
    codeblocks:list[CodeBlock]
    actual_codeblock:Optional[CodeBlock]
    has_main:bool
    def __init__(self):
        self.codeblocks = []
        self.actual_codeblock = None
        self.has_main = False
    def add_codeblock(self, codeblock):
        if not isinstance(codeblock, CodeBlock):
            raise ValueError("codeblock need to be a CodeBlock object")
        if codeblock.name == "MAIN":
            self.has_main = True
        self.actual_codeblock = codeblock
        #if codeblock.name in :
        #    raise NameError("Replicated Name")
        self.codeblocks.append(codeblock)