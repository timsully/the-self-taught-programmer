# Function syntax (python)
# def [function_name]([parameters]):
#     [function_definition]

#def f(x):
#  return x * 2
#f(8)

def f(x):
  return x + 1

z = f(4)

if z == 5:
  print("z is 5")
else:
  print("z is not 5")



# If a function doesn't have a return statement it will return "None"
def f():
  z = 1 + 1

result = f()
print(result)


# len returns the length of an object
len("Monty")


# str function takes an object and returns a new object with a str data type
str(100)


# int function takes an object and returns an integer object
int("1")


# float function takes an object and returns a floating-point number object
float(100)


# input is a built-in function that collects information from the person
# using the program
age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
  print("You are young!")
else:
  print("Wow, you are old!")



# prints whether x is even or odd
def even_odd(x):
  if x % 2 == 0
    print("even")
  else:
    print("odd")

even_odd(2)
even_odd(3)


# Don't use variables defined in a try statement in an except statement,
# because an exception could occur before the variable is defined
# and an exception will get raised inside of your except statement
# when you try to use it:
try:
  10 / 0
  c = "I will never get defined."
except ZeroDivisionError:
  print(c)