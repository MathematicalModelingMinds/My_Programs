Empty_Tuple = ()

# Defining tuples
My_tuple = ('Apple','Banana','Kiwi', 200, 1360)
print(My_tuple)

My_tuple = (3)
print(type(My_tuple))

My_tuple = (3,)
print(type(My_tuple))

My_list = [2,3,'red']
My_tuple = tuple(My_list)
print(My_tuple)

tuple_1 = (4,)*3
print(tuple_1)

# Accessing values
My_tuple = ('Apple','Banana','Kiwi', 200, 1360)
print(My_tuple[0])
print(My_tuple[1:4])

# Concatanate
tuple_1 = (1,2,3)
tuple_2 = ('year','month')
tuple_3 = tuple_1+tuple_2
print(tuple_3)

# Delete
tuple_1 = (1,2,3)
del(tuple_1[0])

tuple_1 = (1,2,3)
del tuple_1
print(tuple_1)

# Length
My_tuple = ('Apple','Banana','Kiwi', 200, 1360)
len(My_tuple)

# Membership
My_tuple = ('Apple','Banana','Kiwi', 200, 1360)
200 in My_tuple

My_tuple = ('Apple','Banana','Kiwi', 200, 1360)
'Mango' in My_tuple

# Min/Max
My_tuple = (23,40,-2,200,0.5)
print(max(My_tuple))
print(min(My_tuple))

# Iterate over values
My_tuple = (2,3,'red')
for i in My_tuple:
    print(i)