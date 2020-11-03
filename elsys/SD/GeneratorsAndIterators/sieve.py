import itertools as it

def sieve(limit, num=it.count(2)):
    p = next(num)
    x = sieve(limit, (n for n in num if n % p))
    yield p
    for _ in range(limit):
        yield next(x)

for x in sieve(10):
    print(f'In "10" series: {x}')

for x in sieve(25):
    print(f'In "25" series: {x}')

for x in sieve(100):
    print(f'In "100" series: {x}')
