# Functions
# Create a function to do only one task

#  2 + 4 + 2 + 5 + 3 + 5 + 4

# Types
# 1. void type -> doesna't return anything
# 2. return type
# Arguments/Parameters (ARGUMENTS)

# Void type

def display(value):
    print(value)


# Return type
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

# (2 + 4) * (3 / 2) -> 

# print(multiply(add(2, 4), divide(3, 2)))

# Create a function that returns a sum of the list

def sumList(list):
    sum = 0
    for num in list:
        sum += num

    return sum

nums = [1, 4, 5, 2, 6]
print(sumList(nums))


fruits = ["Apple", "Banana", "Mango", "Apple", "Banana", "Mango", "Apple", "Banana", "Mango", "Apple", "Banana", "Mango"]

# Create a function to extract a given item

def extractItem(list, item):
    extractItems = []
    for fruit in list:
        if (fruit == item):
            extractItems.append(item)

    return extractItems

print(extractItem(fruits, "Banana"))


# Unknown Arguments
def rollCal(*students):
    print("hi", students)


print(rollCal("David", "Sam", "Mark"))


# Known Arguments
print(extractItem(item="Apple", list=fruits))


# default value in a function
def myFunction(country = "Dubai"):
    print("I live in this county", country)

print(myFunction("Austraila"))

def emptyFunction():
    pass

