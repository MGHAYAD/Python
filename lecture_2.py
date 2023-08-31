

# Input Function
# firstName = input('Enter your first name ')  
# print(firstName)

# Before
# age = input('Enter your age ')
# print(age + 5)

# Type Casting
# Convert one data type into another
# str -> int

# After
# age = int(input('Enter your age '))
# print(age + 5)

# # ASCII (Latin) or UTF-8
# print(chr(105))


# Decision/Conditional Structure
# if 
# else

# Take input from the user as a number
# Check whether that number is an Even or Odd

# Even number is a number that is divisible by 2

# num = int(input('Enter a number'))

# # % -> Remainder

# if num % 2 == 0:
#     print(num, ' is an Even number')
# else:
#     print(num, ' is an Odd number')

# Boolean operators
# AND, OR and NOT


# Take an input as a number from the user
# and check whether that number is divisible by 2 
# or 3 or both

# USE OF AND

# if (num % 2 == 0) and (num % 3 == 0):
#     print(num, ' is divisible by both 2 and 3')
# elif num % 2 == 0:
#     print(num, ' is only divisible by 2')
# elif num % 3 == 0:
#     print(num, ' is only divisible by 3')
# else:
#     print(num, ' is neither divisible by 2 or 3')

# USE OF OR
# if (num % 2 == 0) or (num % 3 == 0):
#     print(num, ' is divisible by either 2 or 3')
# else:
#     print(num, ' is neither divisible by 2 or 3')


# Implement a program that prompts the user to enter
# their exam score and then prints their corresponding
# letter grade based on the following scale: 90-100 (A),
# 80-89 (B), 70-79 (C), 60-69 (D), below 60 (F).

examScore = int(input('Enter your exam score'))

if (examScore (>= )90) and (examScore <= 100):
    print('You got A grade')
elif (examScore >= 80) and (examScore <= 89):
    print('You got B grade')
elif (examScore >= 70) and (examScore <= 79):
    print('You got C grade')
elif (examScore >= 60) and (examScore <= 69):
    print('You got D grade')
else:
    print('Sorry you failed (F)')

