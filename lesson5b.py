# Functions with parameters
# Parameters- They are values that get passed as arguments given to a function inside of the parenthesis


def greetings(name):
    print(f"{name} How are you? Hope everything is fine.")

greetings("Ryan")
greetings("Theo")
greetings("Enzo")

print('===============================')
def message(names):
    print(f"Hello {names}. We shall be having a general meeting on date....Please avail yourself.")

message("Daphnie")
message("Anna")

print('========================')
# Accept parameters to add two numbers
def addition (x, y):
    sum = x + y
    print("The sum is:", sum)

addition(45, 65)
addition(78, 92)
