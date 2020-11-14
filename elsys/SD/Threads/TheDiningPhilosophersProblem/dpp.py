from threading import Thread, Lock, Semaphore
from time import sleep
from enum import IntEnum
from random import randint
import logging


class PhilosopherSyncManager:
    class __Inner:
        def __init__(self):
            self.count = 5
            self.sems = [Semaphore() for _ in range(self.count)]
            self.global_lock = Lock()
            self.states = [PhilosopherStates.THINKING for _ in range(self.count)]

    instance = None

    def __init__(self):
        if not PhilosopherSyncManager.instance:
            PhilosopherSyncManager.instance = PhilosopherSyncManager.__Inner()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def forks_near(self, ph_id):
        return self.forks[ph_id], self.forks[ph_id - 1]

    def ph_near(self, ph_id):
        return (ph_id + 1) % self.count, ph_id - 1

    def ch_state(self, ph_id, new_state):
        if hasattr(PhilosopherStates, new_state):
            self.states[ph_id] = getattr(PhilosopherStates, new_state)
            logging.info(f"{Philosopher.PHILOSOPHER_NAMES[ph_id]} now '{new_state}'.")


class PhilosopherStates(IntEnum):
    THINKING = 0
    EATING = 1
    HUNGRY = 2


class Philosopher(Thread):
    PHILOSOPHER_NAMES = ["(0) Friedrich Nietzsche", "(1) Arthur Schopenhauer", "(2) Immanuel Kant", "(3) Aristotle", "(4) John Locke"]

    def __init__(self, ph_id):
        super().__init__(name=f"Philosopher #{ph_id}")
        self.name = Philosopher.PHILOSOPHER_NAMES[ph_id]
        self.id = ph_id

    def run(self):
        logging.info(f"{Philosopher.PHILOSOPHER_NAMES[self.id]} sits on the table.")
        PhilosopherActivities.loop(self)

    def __getattr__(self, item):
        return getattr(super(), item)


class PhilosopherActivities:

    @classmethod
    def think(cls, ph_id):
        interval = randint(1, 11)
        psync = PhilosopherSyncManager()
        assert psync.states[ph_id] == PhilosopherStates.THINKING, f"states: {psync.states}"
        logging.info(f"{Philosopher.PHILOSOPHER_NAMES[ph_id]} is thinking({interval}s).")
        sleep(interval)

    @classmethod
    def eat(cls, ph_id):
        interval = randint(1, 10)
        psync = PhilosopherSyncManager()
        try:
            assert psync.states[ph_id] == PhilosopherStates.EATING
        except AssertionError:
            print(f"{ph_id} is 'eating' but {psync.states}")
        logging.info(f"{Philosopher.PHILOSOPHER_NAMES[ph_id]} is eating({interval}s).")
        sleep(interval)

    @classmethod
    def take_forks(cls, ph):
        psync = PhilosopherSyncManager()
        with psync.global_lock:
            psync.ch_state(ph.id, 'HUNGRY')
            PhilosopherActivities.consume(ph.id)
        psync.sems[ph.id].acquire()
        logging.info(f"{ph.name} is taking forks.")
        sleep(2)

    @classmethod
    def ret_forks(cls, ph):
        psync = PhilosopherSyncManager()
        with psync.global_lock:
            logging.info(f"{ph.name} is putting forks down.")
            psync.ch_state(ph.id, 'THINKING')
            n, p = psync.ph_near(ph.id)
            PhilosopherActivities.consume(n)
            PhilosopherActivities.consume(p)
        sleep(2)

    @classmethod
    def consume(cls, ph_id):
        psync = PhilosopherSyncManager()
        states = psync.states
        if states[ph_id] == PhilosopherStates.HUNGRY:
            n, p = psync.ph_near(ph_id)
            if states[n] != PhilosopherStates.EATING and states[p] != PhilosopherStates.EATING:
                psync.ch_state(ph_id, 'EATING')
                psync.sems[ph_id].release()
                PhilosopherActivities.eat(ph_id)

    @classmethod
    def loop(cls, ph):
        while True:
            # logging.info("In thread #{}".format(ph.id))
            PhilosopherActivities.think(ph.id)
            PhilosopherActivities.take_forks(ph)
            PhilosopherActivities.ret_forks(ph)
            sleep(1)


class PhilosophersProblem:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)-8s %(message)s')
        logging.info("Start")
        self.philosophers = [Philosopher(i) for i in range(5)]

    def __del__(self):
        logging.info("Finish")

    def __call__(self):
        for p in self.philosophers:
            p.start()

        for p in self.philosophers:
            p.join()


if __name__ == "__main__":
    dpp = PhilosophersProblem()
    dpp()
