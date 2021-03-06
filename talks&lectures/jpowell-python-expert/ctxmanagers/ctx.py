from sqlite3 import connect

# First version
# with connect("python3-dbtest.db") as conn:
#    cur = conn.cursor()
#    cur.execute('create table points (x int, y int)')
#    cur.execute('insert into points (x, y) values(1, 1)')
#    cur.execute('insert into points (x, y) values(2, 1)')
#    cur.execute('insert into points (x, y) values(1, 2)')
#    for row in cur.execute('select x, y from points'):
#        print(row)
#    for row in cur.execute('select sum(x * y) from points'):
#        print(row)
#    cur.execute('drop table points')

# SECOND VERSION
# class contextmanager:
# 
#     def __init__(self, gen):
#         self.gen = gen
#         
#     def __call__(self, *args, **kwargs):
#         self.args, self.kwargs = args, kwargs
#         return self
# 
#     def __enter__(self):
#         self.gen_inst = self.gen(*self.args, **self.kwargs)
#         next(self.gen_inst)
# 
#     def __exit__(self, *args):
#         next(self.gen_inst, None) 

# @contextmanager
# def temptable(cur):
#     cur.execute('create table points (x int, y int)')
#     yield
#     cur.execute('drop table points')
# 
# with connect('python3-dbtest.db') as conn:
#     cur = conn.cursor()
#     with temptable(cur):
#         cur.execute('insert into points (x, y) values(1, 1)')
#         cur.execute('insert into points (x, y) values(1, 2)')
#         cur.execute('insert into points (x, y) values(2, 1)')
#         for row in cur.execute('select x, y from points'):
#             print(row)
#         for row in cur.execute('select sum(x * y) from points'):
#             print(row) 


# THIRD VERSION

from contextlib import contextmanager

@contextmanager
def temptable(cur):
    cur.execute('create table points (x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')

with connect('python3-dbtest.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')

        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row) 


