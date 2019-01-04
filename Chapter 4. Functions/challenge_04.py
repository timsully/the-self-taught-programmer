# Write a program with two functions. The first function should take an 
# integer as a parameter and return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the 
# result of the integer multiplied by 4. Call the first function, save the
# result as a variable, and pass it as a parameter to the second function.
# Pass value into function which will divide it by two and return
def divide_by_two(x):
  return x / 2

value_stored = divide_by_two(6)
print(value_stored)

# Passing the value stored in the variable value_stored into
# function and then multiplying it by 4 and then returning
def anotha_func_breh(int):
  return int * 4

print anotha_func_breh(value_stored)