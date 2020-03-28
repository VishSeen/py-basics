# Integers variable
# ----------------- #

# integer known as int are whole numbers.
# it stores only and only whole numbers.
# you can perform various maths operation on them. 
# more about maths on arithmetic operators.py
# for now just know how to create integers

# To create an integer variable
# first: give it a name
# sec : use the = (equal sign) to assign a value
# third : enter your number
# ------------------- #
# a_num = your value  #
# ------------------- #

number_one = 5
number_two = 10
print(number_one)
print(number_two)
print("-------------")


# creating multiple integer
a, b = 1, 3
print(a)
print(b)
print("-------------")


# assigning value to another variable
# here we create a var named c and tell it to 
# hold the same value as b which is 3
c = b
print(c) 
print("-------------")


# print a, b, c
# you will see that c and b has same value
print(a)
print(b)
print(c)
print("-------------")


# now we change value of b and see what happens to c
b = 2
print(a)
print(b)
print(c)
# as you can see, b has changed and not c.
# this is because both are different variable (boxes).
# which means that if we change something in c,
# b will not be affected and vice-versa.
# when creating c, we told it to save a copy of the value
# of b. As it already saved a copy, changing b will not affect c



# ------------------- #
# UP NEXT : floats.py #
# ------------------- #