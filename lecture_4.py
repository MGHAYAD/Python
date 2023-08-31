# Lists 

fruits = ['Apple', 'Apple', 'Banana', 'Strawberry']

# Dynamic list
items = ['Apple', 0, 2.3, True]

nums = [4, 1, 10, 7, 6]

chars = ['C', 'Q', 'A', 'K', 'B']


# Add more items
fruits.append('Mango')
print(fruits)

# Add at a specfic index
fruits.insert(1, 'Orange')
print(fruits)

# Remove an item based on value
fruits.remove('Apple')
print(fruits)

# Remove item based on index
fruits.pop()
print(fruits)

# Count numeber of 
print(fruits.count('Apple'))

# Sort items in a list
nums.sort(reverse = True)
print(nums)

chars.sort()
print(chars)

# Min and Max
print(min(nums))

# nums.extend([12, 54, 66])
print(nums * 3)