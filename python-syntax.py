## week 1 Day 1 Lecture

## first data type --> Strings

# this is a variable with a string stored in it
first_words = "Hello World!"
print(first_words) # prints "Hellow World" to the terminal

# this is a comment
# It's a line of code that will not be run.

# Can also initiate a string with single quotes ''
new_string = 'Look at that, single quotes'

# Escape charatcer \ allows us to still use single quotes inside of a single quote string
example = 'Can\'t use sing\'le quot\'es inside of si\'ngle quotes'
print(example)

words_with_apostrophes = "can't shan't won't"

# Concatination - combine multiple strings together
string1 = "This is"
string2 = "super cool"

# Concatinate  multiple strings within a new variable
concat = string1 + string2

# concatinate with + sign
print(string1 + " " + string2)

# concatinate with a ,
print(string1, string2)

# Docstring - multiline string

### Incorect format for doc string
# another_string = " 
# line 1
# line 2
# line 3
# "

# initiate a doc string with three ''' either single or double """
doc = '''
Enter 1 to continue
Enter 2 to go back
Enter 3 to figure it all out
'''
print(doc)

# Python reads code from the top to the bottom and so here, we've redefined the variable doc. And so it will print as its new value.
doc = "This new thing"

print(doc)

first, middle, last = "Travis", "Cline", "Peck"
print(middle)

print(first, middle, last)

# Never create variable with reserved words
# global = "this" 
# if = "that"
# Global and if are both words that are already reserved for something else in Python

# print = 'don"t do this'
# print(print)

