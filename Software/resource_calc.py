class ResourceCalculator():
    def __init__(self, max_rom, max_ram):
        if not isinstance(max_rom, int):
            raise TypeError("Parameter must be a Int")
        if not isinstance(max_ram, int):
            raise TypeError("Parameter must be a Int")
        
        self.max_rom = max_rom
        self.max_ram = max_ram
        self.__ram_utilized = 0
        self.__rom_utilized = 0
    def log(self):
        print("\n")
        print(30*"-" + "RECURSOS UTILIZADOS" + 30*"-")
        print(f"ROM:    {self.__rom_utilized} DE {self.max_rom}")
        print(f"RAM:    {self.__ram_utilized} DE {self.max_ram}")
    def increment_utilized_RAM(self, quantity = 1):
        if self.max_ram < (self.__ram_utilized + quantity):
            raise OverflowError("RAM usage exceeds maximum available")
        self.__ram_utilized += quantity

    def increment_utilized_ROM(self, quantity = 1):
        if self.max_rom < (self.__rom_utilized + quantity):
            raise OverflowError("ROM usage exceeds maximum available")
        self.__rom_utilized += quantity