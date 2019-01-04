# Write a function that converts a string to a float and returns the result
# Use exception handling to catch the exception that could occur.
def string_to_float(x):
  try:
    return float(x)
  except ValueError:
    print("Must be a number in string format to convert value to float.")

switch_this = string_to_float("80")
print(switch_this)