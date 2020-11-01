from exceptions import BadBorrow, BadReturn
from random import choice

class LibraryItem:

    def operate(self):
        pass

    def __repr__(self):
        return 'No instances should be created for this class'

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, cc):
        self._count = cc


class BookComponent(LibraryItem):
    
    books = {
                'The Wheel of Time': ('Robert Jordan + Brandon Sanderson', 15),
                'Lord of the Rings': ('J. R. R. Tolkien', 3),
                'The Dark Tower': ('Stephen King', 7),
                'Stormlight\'s Archives': ('Brandon Sanderson', 4),
                'Mistborn Era 1': ('Brandon Sanderson', 3),
                'The Shining': ('Stephen King', 1)
            }

    def __init__(self, nm=None, a=None, n=None):
        super().__init__()
        b = BookComponent.books
        if nm is None:
            nm = choice(list(b))
        self._title = nm
        if a is None:
            a = b[self._title][0]
        self._author = a
        if n is None:
            n = b[self.title][1]
        self._num_of_books = n

    def __repr__(self):
        return 'BookComponent({}, {}, {})'.format(self.title, self.author, self.num_of_books)

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'--- Book entry ---\n'\
               f'{self.title}: ({self.num_of_books} books)\n'\
               f'by {self.author}\n'

    def operate(self): 
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, a):
        self._author = a

    @property
    def num_of_books(self):
        return self._num_of_books

    @num_of_books.setter
    def num_of_books(self, nob):
        self._num_of_books = nob


class MovieComponent(LibraryItem):

    movies = {
                'The Green Mile' : ('Frank Darabont', 1999),
                'The Shining': ('Stanley Kubrick', 1980),
                'The Godfather': ('Francis Copolla', 1972)
            }

    def __init__(self, nm=None, d=None, y=None):
        super().__init__()
        m = MovieComponent.movies
        if nm is None:
            nm = choice(list(m))
        self.title = nm
        if d is None:
            d = m[self.title][0]
        self.director = d
        if y is None:
            y = m[self.title][1]
        self.year = y


    def operate(self):
        pass

    def __eq__(self, other):
        return self.title == other.title

    def __repr__(self):
        return 'MovieComponent()'

    def __str__(self):
        return f'--- Movie entry ---\n'\
               f'{self.title}: {self.year}\n'\
               f'directed by {self.director}\n'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, di):
        self._director = di

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, y):
        self._year = y


class CollectibleComponent(LibraryItem):

    collection = {
            'Stephen King': ('Figure', 'Vinyl'),
            'Roland Dischein': ('Figure', 'Vinyl'),
            'Georgy\'s Boat': ('Boat', 'Paper'),
            'Gandalf': ('Figure', 'Stone')
                }

    def __init__(self, nm=None, w=None, m=None):
        super().__init__()
        c = CollectibleComponent.collection
        if nm is None:
            nm = choice(list(c))
        self.name = nm
        if w is None:
            w = c[self.name][0]
        self.what = w
        if m is None:
            m = c[self.name][1]
        self.material = m

    def __repr__(self):
        return 'CollectibleComponent()'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f'--- Collection entry ---\n'\
               f'{self.name} {self.what.lower()} from {self.material.lower()}\n'

    @property
    def what(self):
        return self._what

    @what.setter
    def what(self, w):
        self._what = w

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, m):
        self._material = m

    def operate(self):
        pass

