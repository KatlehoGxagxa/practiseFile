# Author: Katleho Gxagxa
# Subtraction of integer types.

# Basic subtraction.
# To subtract integers, the '-' operator is used.
a = 10
b = 15
result = a - b
answer = b - a
print(result, answer)

# Subtracting Negative Numbers.
# Keep in mind that subtracting a negative is the same as adding the absolute value of that number.
a = 10
b = -3
result = a - b
print(result)

# Chaining Subtractions.
a = 20
b = 5
c = 2
result = a - b - c
print(result) # This calculates (20 - 5) - 2, resulting in 13.

# Using subtraction in a Loop or Function.
numbers = [2, 4, 6]
start_value = 20
for num in numbers:
    start_value -= num
print(start_value)

# Important Considerations.
# 1. The result of subtracting two integers is always an integer.
# 2. Python supports subtraction of large integers without overflow, as it automatically manages memory for large values.
