context = -1
rom_utilize = 0
filename = input("Introduce el archivo a compilar: ")

file_data = open(filename, "r");

for line in file_data.readlines():
    line = line.strip()
    if line == "":
        continue
    inst = line.split(" ")
    inst_name = inst[0]
    if inst_name.endswith(":"):
        context = inst_name[:-1]
    elif inst_name == "END":
        context = "No context"
    elif len(inst) > 1:
        inst_parameters = inst[1::]
        print(f"La instruccion es: {inst_name} con {len(inst_parameters)} parametros: {inst_parameters} en el contexto {context} en la posicion {rom_utilize}")
        rom_utilize += 1
    else:
        print(f"La instruccion es: {inst_name} en el contexto {context} en la posicion {rom_utilize}")
        rom_utilize += 1

file_data.close()