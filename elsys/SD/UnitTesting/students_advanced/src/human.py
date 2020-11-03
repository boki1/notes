from random import choice, randint
# from phone import Phone
from .phone import Phone


class HumanAddress:
    CITIES = ['Sofia', 'London', 'Sidney']
    STREETS = ["Cedar Court", "4th Street", "South Street", "Oak Street"]

    def __init__(self, _city=None, _street=None, _number=None):
        self.street = _street if _street is not None else choice(HumanAddress.STREETS)
        self.number = _number if _number is not None else randint(1, 100)
        self.city = _city if _city is not None else choice(HumanAddress.CITIES)

    def __str__(self):
        return f'\n\tCity: {self.city}\n' \
               f'\tStreet: {self.street}\n' \
               f'\tStreet number: {self.number}\n'

    def __repr__(self):
        return f'HumanAddress("{self.city}", "{self.street}", "{self.number}")'

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @city.setter
    def city(self, city_name):
        self.__city = city_name

    @street.setter
    def street(self, street_name):
        self.__street = street_name

    @number.setter
    def number(self, number):
        self.__number = number


class Human:
    NAMES = ['Kaylynn', 'Karli', 'Avery', 'Briley',
                 'Amari', 'Ivy', 'Raquel', 'Jordyn']

    def __init__(self, name=None, addr=None, ph=None):
        self.name = name if name is not None else choice(Human.NAMES)
        self.addr = addr if addr is not None else HumanAddress()
        self.phone = ph if ph is not None else Phone()

    def __str__(self):
        return f'Person name: {self.name}\n' \
               f'Person address: {repr(self.addr)}\n' \
               f'Person phone: \n{repr(self.phone)}\n'

    def __repr__(self):
        return f'Human("{self.name}", {repr(self.addr)}, {repr(self.phone)})'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def addr(self):
        return self.__address

    @addr.setter
    def addr(self, addr):
        self.__address = addr

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, val):
        self.__phone = val
