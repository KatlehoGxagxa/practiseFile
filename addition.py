# Author: Katleho Gxagxa

# 1. Basic addition.
# You can add two or more integers using the '+' operator.
a = 5
b = 3
result = a + b
print(result)


# 2. Handling Large Integers.
'''
Python's int type supports arbitrarily large integers.
This means you can add very large numbers without worrying about overflow, unlike some other programming languages where the integer size is fixed.
https://youtu.be/WN8i5cwjkSE

'''
large_num1 = 1983209281712
large_num2 = 1097029347042
result = large_num1 + large_num2
print(result)

# 3. Negative numbers.
# Addition also works with negative numbers.
a = -5 
b = 3
result = a + b
print(result)

# 4. Combining multiple integers
result = 1 + 2 + 3 + 4 + 5
print(result)

# 5. Type Conversion.
# If you add integers with other numeric types, such as floats, Python will perform type conversion.
a = 5
b = 3.2
result = a + b
print(result)

# 6. Using the sum() Function
# Python provides the built-in sum() function for adding a list of numbers.
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)

# 7. In-Place Addition (+= Operator)
# The += operator adds a value to a variable and then assigns the result back to that variable.
a = 5
a += 3
print(a)

# 8. Error Handling.
# Attempting to add a non-numeric type to an integer will raise a TypeError.
a = 5
b = "hello"
print(a + b) 


