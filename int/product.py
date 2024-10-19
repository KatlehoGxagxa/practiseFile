# Author: Katleho Gxagxa.
# The '*' operator is used for multiplication of integers in python.

# Basic Multiplication.
a = 5
b = 3
result = 5 * 3
print(result)


# Mutliplying negative numbers.
# When multipying integers, keep these rules in mind.
# Positive x Positive = Positive.
# Negative x Negative = Positive.
# Positive x Negative = Negative.
a = 5
b = -3
result = a * b
print(result) # negative result.


c = -5
d = -3
result = c * d
print(result) # positive result.

e = 5
f = 3
result = e * f
print(result)

# Using multiplication.
# I compute the product iteratively, from elements in a list.
numbers = [1, 2, 3]
product = 1
for number in numbers: # for every number in the numbers list, multiply that by the product variable. More on loops later.
    product *= number
print(product)

# Python's handiling of large products.
# Python supports multiplication of very large integers, as it automatically manages memory for large values.
a = 123456789
b = 987654321
result = a * b
print(result)

# Important Considerations.
# The result of multiplying two integers is always an integer.
# Multiplying by zero always results in zero.
# Be cautious of overflow in other languages, but python handles large integers seamlessly.