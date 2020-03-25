# Strings variable
# ----------------- #
# strings types are basically texts.
# which means that it only holds texts.
# we use " or ' (single or double quotes)
# in between these we put the text we want
# whenever you see a value inside "" or ''
# know that it is a text (string)

a_string = "Hello Python"
b_string = "Shane"

# if you want to use comma as text
# use double quotes as variable assignement
using_comma_as_text = "it's a good day"

# if you want to use quotes as text
# use single quotes as variable assignement
using_quotes_as_text = '"Hey !" said John..'



# outputs:
# ----------------- #
print("Value for a_string : " + a_string)

print("Value for b_string : " + b_string)

print("Value for using_comma_as_text : " + using_comma_as_text)

print("Value for using_quotes_as_text : " + using_quotes_as_text)

print(" ")



# using built-in methods
# ---------------------- #
# we will use function to manipulate texts
# more on functions in the functions.py file
# for now just understand that function makes it easier to
# manipulate variables
# str() converts whatever whole number inside to type text
# len() return the value of the text inside which is name
# lower() makes text as lower case
# upper() makes text all cap
# count() returns number of times a char is inside the text
# you can even use words
# find() returns the position the char/word is in the sentence

name = "Vishroy Seenarain"

# printing the text in the name variable
print(name)

# printing text as all cap
print("Name in all cap : " + name.upper())

# printing text as lower
print("Name in lower case : " + name.lower())

# printing number of 's' found in name
# using str() as count() returns an integer
# as we are printing a text, the number should be converted to text
print("Number of 'S' in the name variable : " + str(name.count('s')))

# printing length of the text
# same happening here as len() returns an integer type
print("Length of name is : " + str(len(name)))

# printing length of the text
# same happening here as len() returns an integer type
print("Finding position of 'O' : " + str(name.find('o')))

print(" ")


# Friendly reminder
# ---------------------- #
# you should not remember these functions by heart.
# just remember that they are available to you.
# you just need to know how to use them.
# you can always goto the documentation web of python to 
# know what functions are available for you
# web: https://docs.python.org/3/library/stdtypes.html#string-methods