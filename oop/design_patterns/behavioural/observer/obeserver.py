from random import randint 
from time import sleep

class ObserverRegisteredException(Exception):
    def __init__(self, *ctx):
        self.msg = ctx

class ObserverNotRegisteredException(Exception):
    def __init__(self, *ctx):
        self.msg = ctx

class ISubject:

    def __init__(self):
        pass

    def register(self, o):
        pass

    def remove(self, o):
        pass

    def notify_all(self):
        pass


class IObserver:
    
    def __init__(self):
        pass

    def update(self):
        pass


class Subject(ISubject):

    def __init__(self, observers=None, name=None):
        # super class constructor call omitted intentionally
        if observers is None:
            observers = set()
        self.observers = observers
        self.state = True

        if name is None:
            name = "<default subject name>" 
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def register(self, observer):
        if observer in self.observers:
            raise ObserverRegisteredException(f"cannot add {observer}")
        self.observers.add(observer)

    def remove(self, observer):
        if observer not in self.observers:
            raise ObserverNotRegisteredException(f"cannot remove {observer}")
        self.observers.remove(observer)

    def notify_all(self):
        for observer in self.observers:
            observer.update()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nm):
        self.__name = nm

    def loop(self):
        old, r = bool(randint(0, 2)), self.state
        self.__state = r
        if self.state != old:
            self.notify_all()

        sleep(1)
        return self.loop()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, s=False):
        self.__state = s

class Observer(IObserver):

    def __init__(self):
        # super class constructor call omitted intentionally
        self.__subject = None
        self.internal = None

    def attach(self, subject):
        self.subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, s):
        self.__subject = s

    @property
    def istate(self):
        return self.__internal

    @istate.setter
    def istate(self, i):
        self.__internal = i

    def update(self):
        new_state = self.subject.state
        self.istate = new_state
        print(self)
        return self.istate

    def __str__(self):
        return f"State change of {self.subject}: now {self.istate}"


observers = (Observer(), Observer(), Observer())
observable = Subject(observers, "'Gosho subekta'")
for o in observers:
    o.attach(observable)

observable.loop()
