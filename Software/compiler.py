from . import FileReader
from . import Formater
from . import instruction_set
from . import Instruction
from . import ResourceCalculator
from . import CodeBlockController, CodeBlock
filename = input("Introduce el archivo: ")
block_controller = CodeBlockController()
calculator = ResourceCalculator(1024, 255)

#CICLO DE OBTENCION DE FUNCIONES
used_func = ["MAIN", "FUN", "FUN_2", "FUN_3"]
"""while(True):
    for line_count, line in enumerate(FileReader(filename)):
        formated_line = Formater.format(line)
        if formated_line.is_codeblock:
            codeblock_name = Formater.as_codeblock_name(str(formated_line))"""
        

rom_address = 0

errors = []
#CICLO DE COMPILACION Y TRANSFORMACION
for line_count, line in enumerate(FileReader(filename)):
    formated_line = Formater.format(line)
    if formated_line.is_blank or formated_line.is_comment:
        continue
    elif formated_line.is_codeblock:
        codeblock_name = Formater.as_codeblock_name(str(formated_line))
        block_controller.add_codeblock(CodeBlock(codeblock_name, rom_address))
        print(f"La pieza {codeblock_name} empieza en el {rom_address}")
    elif formated_line.is_instruction:
        codeline_arguments = Formater.split(formated_line())
        instruction:str = codeline_arguments.instruction
        if instruction == "END":
            block_controller.actual_codeblock = None
        if instruction in instruction_set.keys():
            instruction_object:Instruction = instruction_set[instruction]
            try:
                if block_controller.actual_codeblock is None:
                    raise RuntimeError("Instruction not are in a valid function")
                if block_controller.actual_codeblock.name in used_func:
                    block_controller.actual_codeblock.add_line(formated_line())
                    instruction_object.to_binary(codeline_arguments.parameters)
                    calculator.increment_utilized_ROM()
                    rom_address += 1
            except Exception as e:
                errors.append(f"Error en {filename}:{line_count + 1} => {str(e)}")
    else:
        print(f"En la linea {line_count + 1} la palabra {codeline_arguments.instruction} no es una instruccion valida")
if not block_controller.has_main:
    errors.append(f"{filename} => Does have a main function")
if len(errors) > 0:
    print("Errores en la compilacion")
    for error in errors:
        print(error)
else:
    print("Compilacion Finalizada")
    calculator.log()