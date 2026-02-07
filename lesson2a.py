# Python List
# A list in python is a collection of items ordered in a certain way.
# A list is introduced by the use of a square brackets[].
# The items of a list are stored inside of indexes. Note: In programming we start counting from index zero(0).
# A list is a mutable i.e the contents of a list can be changed.

cars = [ "BMW" , "Benz" , "McLaren" , "Prado" , "Range" , "Hiance" , "ProBox"]

print(cars)
print(type(cars))

# Accessing items on a list
print(cars[2])
print("The car on index four is:", cars[4])

# List slicing - This is creating a list from a given bigger list
print(cars[0:3])

# List - Mutability
# We use the function append to add an item at the end of the list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove an item at the end of a list
cars.pop()
print(cars)

# We can use an index to add items  to a list
cars[5] = "Pajero"
print(cars)

# We use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)