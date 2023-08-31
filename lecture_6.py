# Loops
# Allows you to perform an action
# certain number of times

# 1. for-loop
# requires a specfic range

# Simple Snytax
# for i in range(1, 100):
#     print('Hello World', i)

# even_list = []
# odd_list = []

# # Finding first 100 Even and odd numbers
# for i in range(1, 101):
#     if (i % 2 == 0):
#         even_list.append(i)
#         # print(i, 'is an even number')
#     else:
#         odd_list.append(i)
#         # print(i, 'is an odd number')

# print(even_list)
# print(odd_list)


# Let's use for loop in lists
fruits = ['Apple', 'Apple', 'Banana', 'Strawberry']

# Built-in count function
print(fruits.count('Apple'))

# Our Count Function
# count = 0 
# for i in range(len(fruits)):
#     if (fruits[i] == 'Apple'):
#         count+=1
#     # print(fruits[i])

# print(count)

# Nested Loops
# Loop inside another loop

nested_nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# [1][1] -> 1
# [1][2] -> 

# print('hello world')
# print('hello world')
# Hello World Hello World
# 
for row in range(len(nested_nums)):
    for col in range(len(nested_nums[row])):
        print(nested_nums[row][col], end=' ')
    print()

# for i in range(5):
#     print('H', end=' ')

# 
# #
# # #
# # # # 
# # # # #

for row in range(5):
    for col in range(5):
        print('#', end=' ')
    print()