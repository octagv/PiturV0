from instruction import *
instruction_set = {
    #INTRUCCIONES DE LITERAL
    "ADDLW": LiteralInstruction(0),
    "SUMLW": LiteralInstruction(1),
    "SUBLW": LiteralInstruction(2),
    "ANDLW": LiteralInstruction(3),
    "ORLW": LiteralInstruction(4),
    "XORLW": LiteralInstruction(5),
    #INSTRUCCIONES DE REGISTRO
    "ADDWR": RegisterInstruction(0),
    "ADDRW": RegisterInstruction(1),
    "SUMWR": RegisterInstruction(2),
    "SUBWR": RegisterInstruction(3),
    "ANDWR": RegisterInstruction(4),
    "ORWR": RegisterInstruction(5),
    "XORWR": RegisterInstruction(6),
    "INCR": RegisterInstruction(7),
    "DECR": RegisterInstruction(8),
    "SHLR": RegisterInstruction(9),
    "SHRR": RegisterInstruction(10),
    "COMPR": RegisterInstruction(11),
    "CMPWR": RegisterInstruction(12),
    "CLRR": RegisterInstruction(13),
    #INSTRUCCIONES CONDICIONALES
    "IF" : ConditionalInstruction(0),
    "IFN" : ConditionalInstruction(0),
    #INSTRUCCIONES DE SALTO
    "GOTO": JumpInstruction(0),
    "CALL": JumpInstruction(1),
    #INSTRUCCIONES ESPECIALES
    "NOP": EspecialInstruction(0),
    "RETURN": EspecialInstruction(1),
    "ADDSTW": EspecialInstruction(2),
    "ADDWST": EspecialInstruction(3),
    "ADDGPW": EspecialInstruction(4),
    "ADDWGP": EspecialInstruction(5)
}

register_set = {
    "PORTA":1,
    "PORTB":1,
    "TRISA":1,
    "TRISB":1,
    "PINA":1,
    "PINB":1,
    "STATUS":1,
    "GP":1,
    "STACK":1,
    "W":1
}