# Tuple
# It is an imutable type of a list( It cannot change)
# To introduce a tuple we use parenthesis()

counties = ("Nairobi" , "Mombasa" , "Nakuru" , "Kisii" , "Eldoret")
print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accessing items of a tuple by use of indexes
print(counties[4])

# Note: Below will generate an error
# Attribut error
counties.append("Macah")
print(counties)