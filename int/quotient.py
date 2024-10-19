# Author: Katleho Gxagxa
# In python, the quotient of integers can be calculated using different division operators depending on the type of result desired.

# 1. Floating-Point Division.
# The '/' operator divides two numbers and returns a floating point (decimal) result, even if both operands are integers.
a = 10 
b = 3
result = a / b
print(result)


# 2. Integer (Floor) Division (// Operator).
# The '//' operator performs integer division, which returns the quotient without the remainder, effectively rounding down to the nearest integer.
# It's also known as floor division because it rounds down towards negative infinity.
a = 10
b = 3
result = a // b
print(result) # result = 3.

# When dividing a positive number by a negative number, or vice versa, the result is rounded down to the nearest lower integer.
a = 10
b = -3
result = a // b
print(result) # result = -4 (rounds down towards negative infinity).


# 3. Modulus (% Operator)
# The modulus operator (%) returns the remainder of the division.

a = 10
b = 3
remainder = a % b
print(remainder) # result = 1

a = 10
b = -3
result = a % b
print(result) # result = -2.

# 4. divmod() 
# Python's divmod() function returns both the quotient and the remainder as a tuple (quotient, remainder).

a = 10
b = 3
quotient, remainder = divmod(10, 3)
print(f"quotient: {quotient}, and remainder: {remainder}.")

'''
Explanation:    
    Quotient: When performing integer division (10 // -3), the result is -4 because Python rounds towards negative infinity.
    Remainder: The remainder is calculated so that the equation 
    a = (b x quotient) + remainder holds true. Here, 
    10 = (-3 * -4) + (-2)
    10 = (-3 * -4) + (-2).
    Thus, divmod(10, -3) returns (-4, -2).
'''


# Important Considerations.
# Division by Zero: Attempting to divide by zero with any of these methods raises a ZeroDivisionError.
# Negative Division: When performing integer division with negative numbers, the quotient is rounded towards negative infinity.
# Precision: For very large integers, Python handles division without overflow, thanks to its support for arbitrarily large integer values.


