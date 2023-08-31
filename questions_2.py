import random

# 2. Create a list of integers. Use a for loop to calculate and print the sum of all the elements in the list.

list = [1, 2, 3, 4, 5]

sum = 0
for num in list:
    # sum = sum + num
    sum += num

print(sum)

# 13. Create a simple guessing game where the
# computer generates a random number and the user
# has to guess it. The computer provides hints
# whether the guess is too high or too low.
# Use a while loop to repeat until the user guesses correctly.

# How to generate a random number?
# Range of the random number?
# while the input != the the random 

# Math library in pyhton?
# Random

randomNum = random.randint(1, 11)
# isRunning = True 

while (True):    
    guessNumber = int(input('Enter the guess number: '))
    
    if (randomNum == guessNumber):
        print('You have guessed the right number')
        break
        # isRunning = False
    elif (guessNumber > randomNum):
        print('Guess number is high')
    else:
        print('Guess number is low')
    