# Ask the user to print a number three times. Then, an if-else statement
# checks if the number is even. If so, it prints n is even.
def even_odd():
  n = input("type a number:")
  n = int(n)
  if n % 2 == 0:
    print("n is even")
  else:
    print("n is odd")


# telling function even_odd to execute three times
even_odd()
even_odd()
even_odd()