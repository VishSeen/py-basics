# Arithmetic Operators
# ------------------- #

# arithmetic operators are basically maths.
# it includes addition, subtraction, multiplication
# division etc.
# they are just maths symbols that we can use to program.
# they can be use with string and integers

# symbols and their operations
# note that I added them in () just so you can 
# see the symbols

# Addition: (+)
# Subtraction: (-)
# Division: (/)
# Multiplication: (*)
# Modulus: (%)
# Exponential: (**)
# Rounded Division: (//)


# Integers
# --------- #
x = 10
y = 2
z = 3

# addition
print( x + y)

# subtraction 
print(x - y)

# division
print(x / y)

# multiplication
print(x * y)

# modulus
# just gives the remainder of the number
print(x % z)

# exponential
# power of first number by second number
print(x ** y)

# rounded division
# divides and rounds down to nearest integer
print(x // z)

print("----------------")



# String
# --------- #
a = "Hello"
b = "python"

# addition
print(a + b)
print("You can also use text in print and then add " + a + b)

# multiplication
# a word can be multiply by a number
print(a * 2)



# Note that python maths operations works like
# maths. which means using BODMAS / PEDMAS
# simply add operations that you want to be prior inside a ()
# you can add many () inside each other depending on the priority
# your operations. the operations will start from the deepest () first.


# first example
print(x - (y * z))
# here the operation is as follow :
# first: y * z
# second: x - (first)
# ans = 4


# second example
print(x + ((y * z) - y))
# here the operation is as follow :
# first: y * z
# second: (first) - y
# third: x + (second)
# ans = 14

# --------------------------------------------- #
# UP NEXT : comparison and logical operators.py #
# --------------------------------------------- #