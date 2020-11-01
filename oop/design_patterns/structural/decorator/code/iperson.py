from random import randint, choice

class IPerson:

    names = [ "Rand'al Thor", 
             "Thorin Oakenshield", 
             "Don Vito Corleone" 
            ]

    def __init__(self, nm=None, a=None):

        if nm is None:
            nm = choice(IPerson.names) 
        self.name = nm

        if a is None:
            a = randint(12, 89)
        self.age = a

    def __repr__(self):
        return f'IPerson({self.name}, {self.age})'

    def __str__(self):
        return f'=== Person ===\n'\
               f'{self.name} (age: {self.age})'

    def collect(self, item, kind):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        self._age = a

