# Change an item in a list by assigning its index to a new object
colors = [ "blue", "green", "yellow" ]
colors
colors[2] = "red"
colors


# Remove the  last item from a list using the method pop
colors = [ "blue", "green", "yellow" ]
colors
item = colors.pop()
item
colors


# You can check if an item is in a list with the keyword in
colors = [ "blue", "green", "yellow" ]
"green" in colors


# Or check if an item is not in a list
colors = [ "blue", "green", "yellow" ]
"black" not in colors


# You can get the size of a list with len()
len(colors)


# How you might use a list in practice
colors = ["purple",
          "orange",
          "green"]


guess = input("Guess a color:")


if guess in colors:
  print("You guessed correctly!")
else:
  print("Wrong! Try again.")


# A tuple is a container that stores objects in a specific order
# There are two syntaxes to create a tuple
my_tuple = tuple()
my_tuple

my_tuple = ()
my_tuple

# To add objects to a tuple, create one with the second syntax ()
rndm = ("Kobe Bryant", 1978, True)
rndm

# this is a tuple
("tuplesky",)

# this is not a tuple
(9) + 1


# Two syntaxes for dictionaries
my_dict = dict()
my_dict

my_dict = {}
my_dict
