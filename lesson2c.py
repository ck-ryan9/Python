# A dictionary is a data type that stores data in terms of key - value pair
# It is introduced by the use of curly braces{}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys

phonebook = {
    "Ryan": "0439743856" ,
    "Jay" : "0786328643" ,
    "Steve" : "0726289722"
}

# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Print Ryan's number
print(phonebook["Ryan"])

print('=========================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" :["PSG", "Barca" , "Argentina"]
}
# Print the second team
print(player["teams"][1])