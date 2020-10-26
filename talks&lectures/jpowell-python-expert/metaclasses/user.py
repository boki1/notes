# user.py

from library import Base

# First version:
# The derived class is enforcing constraint on the base class

# assert hasattr(Base, 'foo'), "no foo method provided in base class"
# 
# class Derived(Base):
# 
#     def bar(self):
#         return self.foo()

# second version:
# the base class is enforcing constraint on the derived class



class Derived(Base):

    def bar(self):
        return 'bar'
