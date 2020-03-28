# Comparison Operators
# ------------------- #

# comparison operators are used to compare.
# they can be used on numbers  and strings
# they return only boolean values.
# you get only true or false.

# symbols and their operations
# note that I added them in () just so you can 
# see the symbols

# Greater Than: (>)
# Less Than: (<)
# Equal To: (==)
# Not Equal To: (!=)
# Greater or Equal To: (>=)
# Less or Equal To: (<=)

a = 10
b = 5
c = 3


# greater than
# returns true if a greater than b else false
print("a greater than b:")
print(a > b)

print(" ")


# less than 
# returns true if a less than b else false
print("a less than b:")
print(a < b)

print(" ")


# equal to 
# returns true if a equals b else false
print("a is equal to b:")
print(a == b)

print(" ")


# not equal to  
# returns true if a is not equals b else false
print("a is not equal to b:")
print(a != b)

print(" ")


# greater than or equal to 
# returns true if one of the two matches the expression 
# else false if both are false
print("a is greater than or equal to b:")
print(a >= b)

print(" ")


# less than or equal to
# returns true if one of the two matches the expression 
# else false if both are false
print("a is less than or equal to b:")
print(a <= b)

print(" ")
print("---------")


# checking if a string matches
# note that if a characters is in uppercase it will return False
x = "test"
y = "Test"
z = "Test"

print("x equals to y:")
print(x == y)

print(" ")

print("y equals to z:")
print(y == z)

# only == or != works for strings
# so make sure to know when to use them

print(" ")
print(" ")
print(" ")





# Logical Operators
# ------------------- #

# logical operators are used to combine 2 or more comparison operators.
# they can be use to be more precise in comparing integers / string.

# symbols and their operations :
# and - returns true if all statements are True
# or - returns tue if at least one of the statements are True
# not - flips the boolean value

a = 10
b = 5
c = 3

# check if one of statement is true
print("one of the 2 statements are true :")
print(a < b and b > c)
# what this does is:
# first: it checks if: a < b (if this is true, it moves to next statement else return false and ignores the next statement)
# second: checks b > c (if first is true, the second is checked)
# returns true if both of the first and second are true. 
# if either one is false, automatically it will return false



print(" ")


# check if one of statement is true
print("one of the 2 statements are true :")
print(a < b or b > c)
# what this does is:
# first: it checks if: a < b (if this is true, True is returned else it moves to next statement)
# second: checks if : b > c (if this is true, True is returned)
# third: this happens if both are the statements returns false


print(" ")


# returns the opposite value
is_true = True
print("Is it true :")
print(not is_true)

print(" ")

# checks if a > b and inverse the value
print("It is true that a is greater than b but using 'not' it will change to false :")
print(not a > b)




# this is an important chapter in programming.
# make sure to understand the logic and try changing things.


# this marks the end of py-basics. 
# try the next chapter.

# ----------------------------------- #
# NEXT CHAPTER :  py-data-structures  #
# ----------------------------------- #