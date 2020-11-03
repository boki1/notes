from random import choice


# We don't really need a class for this.
# I have implemented it this way only as an exercise.
class PhoneNumber:
    PHONE_NUMBERS = ['(283) 307-7179', '(465) 971-4213',
                         '(495) 320-8276', '(958) 458-3019']

    def __init__(self, _number=None):
        self.number = _number if _number is not None else choice(PhoneNumber.PHONE_NUMBERS)

    def __str__(self):
        return 'Phone number {}'.format(self.number)

    def __repr__(self):
        return f'PhoneNumber("{self.number}")'

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, _number):
        self.__number = _number


class Phone:
    PHONE_VENDORS = ['Apple', 'Samsung', 'Nokia', 'Huawei']
    CONNECTION_PROVIDERS = ['MTel', 'Vivacom', 'Telenor']

    def __init__(self, val=None, vendor=None, conn_provider=None):
        self.number = PhoneNumber(val)
        self.vendor = vendor if vendor is not None else choice(Phone.PHONE_VENDORS)
        self.conn_provider = conn_provider if conn_provider is not None else choice(Phone.CONNECTION_PROVIDERS)

    def __str__(self):
        return f'\tPhone vendor: {self.vendor}\n' \
               f'\tPhone connection provider: {self.conn_provider}\n' \
               f'\tPhone number: {self.number}\n'

    def __repr__(self):
        return f'Phone({repr(self.number)}, "{repr(self.vendor)}", "{repr(self.conn_provider)}")'

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val

    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, new_vendor):
        self.__vendor = new_vendor

    @property
    def conn_provider(self):
        return self.__conn_provider

    @conn_provider.setter
    def conn_provider(self, new_conn_provider):
        self.__conn_provider = new_conn_provider
