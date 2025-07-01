from file_reader import FileReader
from formater_line import Formater
from microcontroller import instruction_set
from instruction import Instruction
from resource_calc import ResourceCalculator
filename = input("Introduce el archivo: ")

calculator = ResourceCalculator(1024, 255)
file = FileReader(filename=filename)
line_count = 0
rom_address = 0
code_pieces = {}
for line in file.iter_line():
    line_count += 1
    formated_line = Formater.format(line)
    if formated_line:
        codeline_arguments = Formater.split(formated_line)
        instruction:str = codeline_arguments.instruction 
        if instruction in instruction_set.keys():
            instruction_object:Instruction = instruction_set[instruction]
            try:
                instruction_object.to_binary(codeline_arguments.parameters)
                calculator.increment_utilized_ROM()
                rom_address += 1
            except OverflowError:
                print("Error: Se sobrepaso la cantidad de ROM")
                raise OverflowError()
            except RuntimeError:
                print(f"Error en la linea {line_count}: {line}")
                print(instruction_object.help())
                raise RuntimeError("Invalid parameter for instruction")
            except Exception as e:
                print(f"Error en la linea {line_count}: {line}")
                raise e

        elif instruction.endswith(":"):
            code_pieces[instruction[:-1]] = rom_address
            print(f"La pieza {instruction} empieza en el {rom_address}")
        elif instruction.startswith("#"):
            pass
        else:
            print(f"En la linea {line_count} la palabra {codeline_arguments.instruction} no es una instruccion valida")

if "MAIN" not in code_pieces.keys():
    raise RuntimeError("The program dont have a main function")
else:
    print("Compilacion Finalizada")
    calculator.log()