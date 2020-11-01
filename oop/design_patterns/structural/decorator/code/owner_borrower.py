from iperson import IPerson
from exceptions import BadReturn, BadBorrow


class Owner(IPerson):
    def __init__(self, nm=None, age=None, lib=None):
        super().__init__(nm, age)

        if lib is not None:
            lib.owner = self
        self.library = lib

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f'Owner({self.name}, {self.age}'

    def anonymous_lend(self, item):
        return self.library.pop(item)

    def retrieve(self, item):
        # Mark in lent list
        # Guess kind
        kind = -1
        self.collect(item, kind)

    def collect(self, item, kind):
        self.library.add(item, kind)

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, l):
        self._library = l


class Borrower(Owner):

    def __init__(self, nm=None, a=None, borrowed=None):
        super().__init__(nm, a)
        if borrowed is None:
            borrowed = {}
        self.borrowed = borrowed

    def __repr__(self):
        return super().__repr__()

    @property
    def borrowed(self):
        return self._borrowed

    @borrowed.setter
    def borrowed(self, b):
        self._borrowed = b

    def borrow(self, lender, item):
        try:
            r = lender.anonymous_lend(item)
        except BadBorrow:
            raise BadBorrow
        else:
            if lender not in self.borrowed:
                self.borrowed[lender] = []
            self.borrowed[lender].append(r)

    def give_back(self, lender, item):
        if lender not in self.borrowed:
            raise BadReturn()
        try:
            self._borrowed[lender].remove(item)
            lender.retrieve(item)
        except ValueError:
            return False
        else:
            return True
