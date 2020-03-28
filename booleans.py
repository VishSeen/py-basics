# Booleans variable
# ----------------- #

# booleans are True or False values.
# in others words, they are only 0 or 1
# they can only hold either True or False
# for booleans variable, be sure to name them well
# so that the name seems like a question and
# the value (True / False) like the answer


# To create a boolean variable
# first: give it a name
# sec : use the = (equal sign) to assign a value
# third : enter your value (True / False)
# ----------------------- #
# a_boolean = your value  #
# ----------------------- #

is_true = True
is_false = False

had_breakfast = False
is_dinner_ready = True


# Outputs
# ---------------------- #
print(had_breakfast)
print(is_dinner_ready)
print("--------------")


# Built-in methods
# ---------------------- #
# bool() evaluates value inside of () to True / False
# isinstance() check if a variable is of any datatype (int, string etc)

# using bool()
# if a string is added inside, it will be true except
# if the string is blank.
# if you evaluate a number, any number will print true except 0
a_string = "Hello"
print(bool(a_string))

a_blank_string = ""
print(bool(a_blank_string))

a_number = 3
print(bool(a_number))

a_zero = 0
print(bool(a_zero))

print("--------------")


# using isinstance()
# this function takes two values inside ()
# first : your variable
# second : data type you wish to check
x = 20
print(isinstance(x, int)) # true if x is an int (Integer)
print(isinstance(x, str)) # false as x is not bool (Boolean)

# NOTE: always separate with , if more than one
# values are needed inside ( )


# more about booleans in flow control chapter.
# you will learn how useful they can be



# --------------------------------- #
# UP NEXT : arithmetic operators.py #
# --------------------------------- #