# for x in collection:
#     pass


# collection = iter(xs)                                 -> __iter__
# while True:
#     x = next(collection)                              -> __next__

from time import sleep

class Compute:

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

for x in Compute():
    print(x)
