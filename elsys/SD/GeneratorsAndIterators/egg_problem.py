import argparse
from random import randint


class EggProblemSolvingAlgorithm:

    def solution(self):
        pass

    def display_step(self):
        pass


class DecreasingIntervalAlgorithm(EggProblemSolvingAlgorithm):

    def __init__(self, eggs=2, floors=100, interval=10):
        self.__eggs = eggs
        self.__floors = floors
        self.interval = interval

        self.__solution = randint(0, self.__floors)
        self.status = 1, False

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, i):
        self._interval = i

    @property
    def current_floor(self):
        return self.__current_floor

    @property
    def current_egg(self):
        return self.status[0]

    def __iter__(self):
        self.__current_step = self.interval
        self.__current_floor = self.interval
        return self

    def advance(self):
        if self.__current_floor >= self.__solution:
            self.status = self.status[0] + 1, False
            self.__current_floor -= self.__current_step
            self.__current_step = 1
            if self.status[0] > self.__eggs:
                self.status = self.status[0] - 1, True
        if self.__current_step > 1:
            self.__current_step -= 1
        self.__current_floor += self.__current_step

    def __next__(self):
        self.advance()
        if self.status[1]:
            raise StopIteration
        return self.status


class Solver:

    def __init__(self, e=None, f=None, a: EggProblemSolvingAlgorithm = None):
        self.eggs = 2 if e is None else e
        self.floors = 100 if f is None else f
        self.strategy = DecreasingIntervalAlgorithm(e, f, 14) if a is None else a
        self.__log_last_step = ''

    @property
    def eggs(self):
        return self._eggs

    @eggs.setter
    def eggs(self, e):
        if e is None:
            e = 2
        self._eggs = e

    @property
    def floors(self):
        return self._floor

    @floors.setter
    def floors(self, f):
        if f is None:
            f = 100
        self._floor = f

    def solution(self):
        strategy_steps = iter(self.strategy)
        while True:
            self.display_step()
            try:
                step = next(strategy_steps)
            except StopIteration:
                yield None
                self.display_step()
                break
            else:
                yield step

    def display_step(self):
        self.__log_last_step = f'Floor #{self.strategy.current_floor}, Egg #{self.strategy.current_egg}, ' \
                               f'Solution found? {self.strategy.status[1]}'
        print(self.__log_last_step)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--floors', metavar='FLOORS', type=int, help='the total number of floors')
    parser.add_argument('--eggs', metavar='EGGS', type=int, help='the total number of eggs')

    args = parser.parse_args()
    eggs, floors = args.eggs, args.floors

    solver = Solver(eggs, floors, DecreasingIntervalAlgorithm())
    for step in solver.solution():
        pass

if __name__ == "__main__":
    main()
