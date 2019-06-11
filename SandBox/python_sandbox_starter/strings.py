
# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'David'
age = 21

# concatenate

#print('Hello, my name is' + name + 'and i am' + str(age))

# String Formatting



#Arguments by position
#print('My name is {name} and i am {age}'.format(name=name, age=age))


#F-strings (3.6+)
#print(f'Hello my name is {name} and i am {age}')


# String Methods

s = 'hello world'


#capitalize string
print(s.capitalize())