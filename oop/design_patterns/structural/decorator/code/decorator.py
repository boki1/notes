from library import Library
from exceptions import BadBorrow, BadReturn
from components import BookComponent, CollectibleComponent, MovieComponent
from owner_borrower import Owner, Borrower


def main():
    lib = Library()
    b, m, c = [], [], []

    for _ in range(10):
        b.append(BookComponent())
        m.append(MovieComponent())
        c.append(CollectibleComponent())
    lib.books = b
    lib.movies = m
    lib.collectibles = c
    # print(lib)

    p = Owner(nm="Oli Olive", age=13, lib=lib)
    # print(p)

    b, db = Borrower(), Borrower()
    try:
        b.borrow(p, BookComponent("The Shining"))
        db.borrow(b, BookComponent("The Shining"))

        b.give_back(b, "The Shining")
        db.give_back(b, "The Shining")

        # This last one should raise an exception
        db.borrow(b, "The Shining")
    except BadBorrow:
        print("Borrow failed.")
    except BadReturn:
        print("Return failed.")
    else:
        print("Successful operation.")


if __name__ == "__main__":
    main()
