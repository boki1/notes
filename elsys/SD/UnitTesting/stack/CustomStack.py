class CustomStack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    @property
    def elements(self):
        return self.__arr

    @elements.setter
    def elements(self, a):
        self.__arr = a
