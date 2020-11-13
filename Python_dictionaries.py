# Empty dictionary
Empty_dict = {}

# Define a dectionary. print keys and values
D = {'Fruit':'apple','color':'red','weight':200}
print(D)
print(D.keys())
print(D.values())

# print the value of a given key
print(D['color'])

# If you tru to access a key that is not available, 
# then you get an error
print(D['name'])

# Update a value
D['color']='green'
print(D)

# Add new pairs
D['price']=10
print(D)

# delete items
D={'fruits':'apple','color':'red','weight':200}
del(D['color'])
print(D)

# duplication of keys
D={'fruits':'apple','color':'red','weight':200,'fruits':'mango'}
print(D['fruits'])

# No lists are accepted as keys
D = {['fruit']:'apple','color':'red'}

# Length of a dictionary
D={'fruits':'apple','color':'red','weight':200}
len(D)

# Key, value pairs as tuples
D.items()

# Iterate over key, value pairs
D={'fruits':'apple','color':'red','weight':200}
for key,value in D.items():
    print('keys:')
    print(key)
    print('values:')
    print(value)
    print(' ')