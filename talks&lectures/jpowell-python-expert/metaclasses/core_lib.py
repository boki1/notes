# core_library.py

# First version:
# the derived class is enforcing constraint on the base class
# class Base:
# 
#     def foo(self):
#         return 'foo'
# 

# SECOND version:
# the base class is enforcing constraint on the derived class

# old_bc = __build_class__
# def my_bc(func, body, base=None, **kw):
#     if base is Base:
#         print('check if the bar method is defined')
#     if base is not None:
#         return old_bc(func, body, base, **kw)
#     return old_bc(func, body, *kw)
# 
# import builtins
# builtins.__build_class__ = my_bc
# 
# class Base:
#     def foo(self):
#         return self.bar()

class BaseMeta(type):

    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        if 'bar' not in body:
            raise TypeError("bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):

    def foo(self):
        return self.bar()
