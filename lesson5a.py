# Python Function
# They are a block of code/statements that perform a given task/action. They can be reused through out the program to perform diff functions
# They are defined by the def key word
# We have 2 main types i.e:
# 1. Inbuilt functions- They come pre-installed with the interpreter i.e print(), pop(), range(), append() 
# 2. User-defined - They are craeted by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis
# For the functions, it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello, How are you?")

# Below we call the function by use of its name
greetings()

print('---------------------------')
# Additional Functions
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:", sum)

addition()
# Craete a function to multiply 3 values
def multiplication():
    num1 = 2
    num2 = 3
    num3 = 4
    multiple = num1 * num2 * num3
    print("The product is:", multiple)

multiplication()
    

print('========================')
# Division function
def divide():
    number1 = int(input("Enter first number:  "))
    number2 = int(input("Enter second number:  "))
    quotient = number1 / number2
    print("The answer is:", quotient)
    print("-----------")

divide()

for function in range(3):
    divide()