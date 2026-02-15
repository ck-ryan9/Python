# Loops - sometimes we may need to do a piece of work a number of repeated times in such cases we may use loops
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops: for loop and while loop

# Below is the syntax of a loop in python:
"""
for variable in range(n):
    #block of code to be executed
"""


for greeting in range(5):
    print("HellO Moses" , greeting)


print('=========================')

for number in range(10, 20):
    print(number)


print('=============================')
# Find even numbers from 50-71
for number in range(50, 71, 2):
    print(number)


print('==========================')
# odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)



print('.............................')
# print multiples of three starting from 201 to 150
for number in range(201, 149, -3):
        print(number)



print('.............................')
# create the leap years in between 2000 ang 2024
for number in range(2000, 2025, 4):
     print(number)
