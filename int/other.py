# Author: Katleho Gxagxa.
# Here I explore the absolute value of an integer. Converting to an integer type using int() and the pow() funtion.

# The abs() function in Python is used to get the absolute value of a number. The absolute value of a number is its non-negative value, 
# regardless of its original sign.

# Basic Usage of abs()
# Syntax: abs(number)
# The function takes a single argument, which can be an integer, a floating-point number, or a complex number.
# The result is always a non-negative value.

# 1. Using abs() with integers.
print(abs(10))
print(abs(-10))

# 2. Using abs() with FLoating-Point Numbers.
print(abs(3.14))
print(abs(-3.14))

# 3. Using abs() with Complex Numbers.
# For complex numbers, abs() returns the magnitude (distance from the origin) of the complex number.
complex_num = 3 + 4j
print(abs(complex_num))


# Using the int() function.
# The int() function in Python is used to convert a value to an integer. It can take numbers, strings, or even other data types 
# and attempt to convert them to an integer type.

# Basic usage of int()
# Syntax: int(value, base)
    # value: the data to be converted to an integer.
    # base: An optional parameter that specifies the number base (radix) for conversion when the value is a string. the default is 10.

# 1. Converting Floating-Point Numbers.
# When converting a float to an integer, int() truncates the decimal portion (it doesn't round).

print(int(3.99)) # Truncation means that the result is only the integer part of a floating-point number and the decimal is discarded.
print(int(-2.5))

# 2. Converting Strings.
# A string can be converted to an integer if it represents a valid number.
print(int("42")) # Here int() might be checking if the string is a valid number, using the .isnumeric() method?
print(int("-100"))

# 3. Specifying a Base for String Conversion.
# If the string represents a number in a different base, you can specify that base.
print(int("1010", 2))
print(int("A", 16))


# 4. Using int() Without Arguments.
# If no arguments are provided, int() returns 0 by default.
print(int())


# Important Considerations.
# 1. Invalid Conversion: if the value, is not a valid integer string or number, Python raises a ValueError.

# Example.
# print(int("hello")) raises a ValueError.

# 2. Converting float("inf"): Trying to convert infinity (float('inf')) to an integer raises an OverflowError.

# Practical Uses of int()
# Parsing User Input: When getting input from a user, which usually comes in as string, int() can be used to convert it to an integer.
# Base Conversion: Useful for converting numbers from different bases (e.g., binary, hexadeximal) to a decimal integer.
# Truncating Floats: Used to truncate the decimal part of a floating-point number.


