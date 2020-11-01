from enum import IntEnum


class Library:

    class Kinds(IntEnum):
        Movie = 1
        Book = 2
        Collectible = 3

    def __init__(self, s=None):
        if s is None:
            s = ""
        self.content = dict()
        self.owner = None

    def __repr__(self):
        return f'Library({self.owner}, {self.books}, {self.movies}, {self.collectibles})'

    def __str__(self):
        _str = f'=== Library ===\n'
        for el in self.books:
            _str += f'\t{el}'
        for el in self.movies:
            _str += f'\t{el}'
        for el in self.collectibles:
            _str += f'\t{el}'
        return _str

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, o):
        self._owner = o

    @property
    def books(self):
        return self.content[Library.Kinds.Book]

    @books.setter
    def books(self, b):
        self.content[Library.Kinds.Book] = b

    @property
    def movies(self):
        return self.content[Library.Kinds.Movie]

    @movies.setter
    def movies(self, m):
        self.content[Library.Kinds.Movie] = m

    @property
    def collectibles(self):
        return self.content[Library.Kinds.Collectible]

    @collectibles.setter
    def collectibles(self, c):
        self.content[Library.Kinds.Collectible] = c

    def lookup(self, item):
        for i, category in self.content.items():
            if item in category:
                return category

    def pop(self, item, kind=None):
        category = None
        if kind is None or \
                item not in self.content[kind]:
            category = self.lookup(item)

        if category is None:
            return None
        return category.remove(item)

    def add(self, item, kind):
        self.content[kind].append(item)



