**Exception handling**

_Universal_

> "... anomalous or exceptional conditions requiring special processing - during the execution of a program."

> "In general, an exception breaks the normal flow of execution and executes a pre-registered exception handler"

-- Wikipedia

_Python specific_

In Python exception handling follows this structure:
```python3

try:
	# Line(s) which might raise an exception
except ExceptionA:
	# Code to be executed on occurance of specific exception
except ExceptionB:
	# Code to be executed on occurance of specific exception
else:
	# Code executed if no exception occurs
finally:
	# Code which will execute everytime LAST

```

**Error handling**

> "Error detection is the detection of errors caused by noise or other impairments during transmission from the transmitter to the receiver"

-- Wikipedia

Or said in Python,

```python3
err_code = some_function_which_might_fail()
if err_code == NOT_FAILED:
	print("We are fine")
elif err_code == FAILED_THIS_BAD:
	print("We are not fine. We are this bad.")
elif err_code == FAILED_THAT_BAD:
	print("We are not fine. We are that bad.")
elif err_code == FAILED_SOMEWHAT_BAD:
	print("We might be fine... or not")
else:
	print("We don't know how bad we are")
```

**Why would we prefer to use error over exception handling?**

Well, to raise an exception there needs to be class deriving from `Exception`. Classes are heavy and slow. And if we have some small check we might want to consider using a normal 0 or -1 return value to signal the state.
