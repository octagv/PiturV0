from abc import ABC, abstractmethod

class Instruction(ABC):
    def __init__(self):
        self.num_of_parameter = 0
        self.optocode = 0b0
    @abstractmethod
    def help(self):
        pass
    @abstractmethod
    def to_binary(self, parameters):
        pass

class JumpInstruction(Instruction):
    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be a Int")
        if id not in (0,1):
            raise ValueError("Id only must be 0 or 1")
        super().__init__()
        self.num_of_parameter = 1
        self.optocode = 0x1000
        self.id = id
    def help(self):
        return "FORMATO:  INSTRUCTION DIR"
    def to_binary(self, parameters):
        if len(parameters) == self.num_of_parameter:
            if not  (0 <= int(parameters[0]) <= 1023):
                raise ValueError("The parameter dont have a valid addres")
            return self.optocode | (self.id << 11) | int(parameters[0])
        else:
            raise RuntimeError("The instruction dont have the necesary parameters")

class ConditionalInstruction(Instruction):
    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be a Int")
        if id not in (0,1):
            raise ValueError("Id only must be 0 or 1")
        super().__init__()
    
        self.num_of_parameter = 2
        self.optocode = 0x2000
        self.id = id
    def help(self):
        return "FORMATO: INSTRUCTION BIT REGISTER"
    def to_binary(self, parameters):
        if len(parameters) == self.num_of_parameter:
            if not ( 0 <= int(parameters[0]) <= 7):
                raise ValueError("The first parameter dont have a valid bit selector")
            if not (0 <= int(parameters[1]) <= 511):
                raise ValueError("Second Parameter is not a valid number")
            return self.optocode | (self.id << 12) | ( int(parameters[0]) << 9) | int(parameters[1])
        else:
            raise RuntimeError("The instruction dont have the necesary parameters")

class LiteralInstruction(Instruction):
    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be a Int")
        if  not (0 <= id <= 5):
            raise ValueError("Id not are valid")
        super().__init__()
        
        self.num_of_parameter = 1
        self.optocode = 0x0800
        self.id = id
    def help(self):
        return "FORMATO: INSTRUCTION LITERAL"
    def to_binary(self, parameters):
        if len(parameters) == self.num_of_parameter:
            if not (0 <= int(parameters[0]) <= 511):
                raise ValueError("Second Parameter is not a valid number")
            return self.optocode | (self.id << 8) | int(parameters[0])
        else:
            raise RuntimeError("The instruction dont have the necesary parameters")
        
class RegisterInstruction(Instruction):
    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be a Int")
        if  not (0 <= id <= 13):
            raise ValueError("Id not are valid")
        
        super().__init__()
        self.num_of_parameter = 2
        self.optocode = 0x4000
        self.id = id
        if id in (0,1,7,8,9,10,11,12,13):
            self.num_of_parameter = 1
    def help(self):
        if self.num_of_parameter == 1:
            return "FORMATO: INSTRUCTION REGISTER"
        else:
            return "FORMATO: INSTRUCTION TARGET REGISTER"
    def to_binary(self, parameters):
        if len(parameters) == self.num_of_parameter:
            if self.num_of_parameter == 1:
                if not (0 <= int(parameters[0]) <= 511):
                    raise ValueError("Second Parameter is not a valid number")
                return self.optocode | (self.id << 10) | int(parameters[0])
            else:
                if int(parameters[0]) not in (0,1):
                    raise ValueError("The first parameter need to be 0 or 1")
                if not (0 <= int(parameters[1]) <= 511):
                    raise ValueError("Second Parameter is not a valid number")
                return self.optocode | (self.id << 10) | int(parameters[0]) << 9 | int(parameters[1])
        else:
            raise RuntimeError("The instruction dont have the necesary parameters")

class EspecialInstruction(Instruction):
    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be a Int")
        if  not (0 <= id <= 5):
            raise ValueError("Id not are valid")
        super().__init__()
        self.num_of_parameter = 0
        self.optocode = 0x0000
        self.id = id

    def help(self):
        return "FORMATO: INSTRUCTION"
    
    def to_binary(self, parameters):
        if len(parameters) == self.num_of_parameter:
            return  self.optocode | self.id
        else:
            raise RuntimeError("The instruction dont have the necesary parameters")