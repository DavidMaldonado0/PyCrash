# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#Individual Assignments

#x = 1           #int
#y = 2.5         #float
#name = 'David'   #str
#is_nice = True  #bool

# Multiple assignment

x, y, name, is_nice = (1, 2.5, 'David', True)

#basic math
a = x + y

#print
print (x, y, name, is_nice, a)

print(type(x))

#casting

x = str(x)
y = int(y)
z = float(y)

print(type(x))
print(type(y), y)
print(type(z), z)