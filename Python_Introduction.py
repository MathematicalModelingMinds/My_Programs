
# Variables and data types
name = "wathsala"
print(type(name))
email = "wath.mali@gmail.com"
print(type(email))
age = 35
print(type(age))

# Numbers
x = 12
y = 65525*65525
z = 23.987
a = 3.2e-6j
print(type(x))
print(type(y))
print(type(z))
print(type(a))

# Strings
name_1 = "wathsala perera"
name_2 = 'wathsala perera'
print(type(name_1))
print(type(name_2))

# Lists
My_list = [1, 5, 7, 'red', 23.8, 'red+yellow']
print(My_list)
print(My_list[2])

# Dictionaries
My_dictionary = {'color':'red','shape':'circle','line':'solid'}
print(My_dictionary)
print(My_dictionary.keys())
print(My_dictionary.values())
print(My_dictionary['shape'])

# Tuples
My_tuple = (1, 5, 7, 'red', 23.8, 'red+yellow')
print(My_tuple)
print(My_tuple[2])

# Tuples cannot be changed.
My_tuple = (1, 5, 7, 'red', 23.8, 'red+yellow')
My_tuple[2]=100