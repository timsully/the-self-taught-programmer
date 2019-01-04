# Write a function that converts a string to a float and returns the result
# Use exception handling to catch the exception that could occur.
# Function that converts a string to a float using exception handling
def string_to_float(x):
  try:
    return float(x)
  except ValueError:
    print("Must be a number in string format to convert value to float.")

# Assigning value to a variable to print
switch_this = string_to_float("80")
print(switch_this)