This week's topic of interest is unit testing.

_Universal_
Unit testing is the process of `testing` your code with simple functions/methods. It should be done in a separate class.

A consideration to keep in mind is that tests should be **light**, since they are executed on each build (best case), and they should also **not be interconnected**.

_Python only_
For python the `unittest` module is used. The simplest example of unit testing would be have a class which derives from `unittest.TestCase` with some methods which have names prefixed with "test".

That's the gist of it.
