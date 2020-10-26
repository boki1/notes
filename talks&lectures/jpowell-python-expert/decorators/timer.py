from time import time

def timer(func):
    def f(*args, **kwargs):
        begin = time()        
        rv = func(*args, **kwargs)
        end = time()
        elapsed = end - begin
        print(f'started {begin}; ended {end}; elapse {elapsed};')
        return rv
    return f

@timer
def add(x, y=10):
    return x + y

@timer
def sub(x, y=10):
    return x - y

print(f'2 + 3 = {add(2, 3)}')
print(f'2 - DEFAULT = {sub(2)}')

