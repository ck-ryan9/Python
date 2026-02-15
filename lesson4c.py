# A for loop can also be used to iterate through a list, tuple, string or even a dictionary..

name = "Ryan" 

for letter in name:
    if letter =="n":
       print("This is a letter n")
    else:
       print(letter)

print('...................')
# Below is a list of counties
counties = {"Nairobi", "Mombasa", "Kisumu", "Machakos", "Eldoret", "Nakuru", "Meru", "Embu", "Kajiado"}

print(counties)

for county in counties:
   print(county)

print('..................................')
for county in counties:
   if county == "Nairobi":
      print("The county is part of the list")
      break
   else:
      print("The county is not part of the list")

print('======================')
# The for loop can also be used to iterate through a dictionary

player = {
   "name": "Ryan",
   "teams": {"Man U" , "Barca"},
   "nationality": "Kenya"
}

for key in player:
   print(key)

print('=======================')
for value in player:
   print(player[value])

print('======================')
# loop through the teams the player has played for
print(player["teams"])
   
for team in player["teams"]:
   print(team)