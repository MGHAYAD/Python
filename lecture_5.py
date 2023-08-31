# Tuples

colors = ('Red', 'White', 'Black')

rbg = (255, 255, 255)

# Length property
print(len(colors))

num = 3

print(type(num))


# Sets
# {a, c , d} U {b, e, w}
# {a, c , d, b, e, w}

# True -> 1 , False -> 0
nums = {1, 2, 3, 4, 5, False}
nums_2 = {4, 5, 6, 7, 8, 9}

print(nums)

union =  nums.union(nums_2)
print(union)

intersection = nums.intersection(nums_2)
print(intersection)

difference = nums_2.difference(nums)
print(difference)

# Add a new element
nums.add(76)
print(nums)

# Remove an new element
nums.remove(76)
print(nums)

nums.update([7, 8, 9])
print(nums)

# Dictionary -> json