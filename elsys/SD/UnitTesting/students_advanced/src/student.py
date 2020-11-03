from random import randint

from .markbook import MarkBook
from .computer import Computer
from .human import Human


class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.id = randint(0, 0x0200)
        self.marks = MarkBook()
        self.computer = Computer()

    def __str__(self):
        header = '\n' + ('='.join(['=' for _ in range(10)])) + '\n'
        tmp_super = super().__str__()
        tmp =  f'Student id: {self.id}\n' \
               f'Student marks: {str(self.marks)}\n' \
               f'Student computer: \n{str(self.computer)}\n'
        return header + tmp_super + tmp + header + '\n'

    @property
    def id(self):
        return self.__id_number

    @property
    def marks(self):
        return self.__marks

    @property
    def computer(self):
        return self.__computer

    @id.setter
    def id(self, id_number):
        self.__id_number = id_number

    @marks.setter
    def marks(self, marks):
        self.__marks = marks

    @computer.setter
    def computer(self, computer):
        self.__computer = computer
