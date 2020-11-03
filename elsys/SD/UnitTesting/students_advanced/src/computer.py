from random import choice, randint


class Computer:
    CPUS = ['Intel', 'AMD']
    VENDORS = ['HP', 'Asus', 'Lenovo']
    RAMS = [8, 16, 24, 32, 64]
    STORAGES = {'SSD': (128, 256, 512), 'HD': (512, 1024, 2048)}

    def __init__(self):
        self.cpu = choice(Computer.CPUS)
        self.mark = choice(Computer.VENDORS)
        self.year = int(''.join([str(randint(1, 10)) for _ in range(4)]))
        self.os = 'Linux'
        self.ram = f'{str(choice(Computer.RAMS))} GB'

        random_storage_device = str(choice(list(Computer.STORAGES.keys())))
        random_storage_size = str(choice(list(Computer.STORAGES[random_storage_device])))
        self.__disk = f'{random_storage_device} ({random_storage_size} GB)'

    def __str__(self):
        return f'\tMark: {self.mark}\n' \
               f'\tCPU: {self.cpu}\n' \
               f'\tYear: {self.year}\n' \
               f'\tOS: {self.os}\n' \
               f'\tRAM: {self.ram}\n'

    @property
    def cpu(self):
        return self.__cpu

    @property
    def mark(self):
        return self.__mark

    @property
    def year(self):
        return self.__year_of_producing

    @property
    def os(self):
        return self.__os

    @property
    def ram(self):
        return self.__ram

    @cpu.setter
    def cpu(self, new_cpu):
        self.__cpu = new_cpu

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark

    @year.setter
    def year(self, new_year):
        self.__year_of_producing = new_year

    @os.setter
    def os(self, new_os="Arch Linux"):
        self.__os = new_os

    @ram.setter
    def ram(self, new_ram):
        self.__ram = new_ram

