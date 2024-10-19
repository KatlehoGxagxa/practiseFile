# This program is about the integer object/type in python.
# Integers have unlimited precision.
# docs.python.org
# with some help from chatGPT.

'''
In Python, "unlimited precision" for integers means that the int type can handle very large numbers without being constrained by a fixed number of bits. 
Unlike some programming languages where integers are limited to a specific size (like 32-bit or 64-bit), 
Python's int type can grow as large as the memory available allows.

This feature makes Python particularly useful for tasks that involve very large integers, such as cryptography, scientific computing, or combinatorial mathematics.
'''

'''
Numbers are created by numeric literals or as the result of built-in functions and operators. 
Unadorned integer literals (including hex, octal and binary numbers) yield integers. 
Numeric literals containing a decimal point or an exponent sign yield floating-point numbers. 
Appending 'j' or 'J' to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts.
print(5j) == 5j
'''

# The contructor int() can be used to produce numbers of a specific type.

# Operations supported for integers. or the int type.
# x + y -> sum of x and y.
# x - y -> difference of x and y.
# x * y -> product of x and y.
# x / y -> quotient of x and y.
# x // y -> floored quotient of x and y.
# x % y -> remainder of x / y.
# -x -> x negated.
# +x -> x unchanged.
# abs(x) -> absolute value or magnitude of x.
# int(x) -> x converted to integer.
# divmod(x, y) -> the pair (x // y, x % y)
# pow(x, y) -> x to the power y.
# x ** y -> x to the power y.


'''
Conversion from float to int truncates, discarding the fractional part. See functions math.floor() and math.ceil() for alternative conversions.
x = 2.5
print(int(x))

'''

'''
Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for programming languages.

print(pow(0, 0)) == 1
print(0 ** 0) == 1

'''

# Bitwise Operations on Integer Types.
    # TODO

# Additional Methods on Integer Types.
    # TODO

    