# Optional parameters let the caller of the function pass in a parameter
# if necessary, but it is not required. If an optional parameter is not
# passed in, the function will use its default value instead. Example:
def f(x=2):
  return x**x

print(f())
print(f(4))


# You can define a function that has both required and optional parameters,
# but you must define all the required parameters before the optional ones.
def add_it(x, y=10):
  return x + y

result = add_it(2)
print(result)


# Writing to a global variable from inside a function
x = 100

def f():
  global x
  x += 1
  print(x)

f()


# Try clause: if you think your code may raise an exception, use an exception,
# use a compound statement with the keywords try and except to catch it.
a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
# try clause contains the error that could occur
try:
  print(a / b)
# the except clause contains code that will ony execute if the exception
# in your try clause occurs
except ZeroDivisionError:
  print("b cannot be zero.")


# You can have your except statement catch two exceptions by adding parentheses
# aroun except and separating the exceptions with a comma:
try:
  a = input("type a number:")
  b = input("type another:")
  a = int(a)
  b = int(b)
except(ZeroDivisionError, ValueError):
  print("Invalid input.")
