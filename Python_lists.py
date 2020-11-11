# Define the list
my_list = [2,3,6,-5,10,'apple']
print(my_list)

num_list = list(range(1,6))
print(num_list)

# Indexing
my_list[0]
my_list[5]

# Negative indexing starts from the end of the list
my_list[-1]
my_list[-2]

# Range of indexes
my_list[2:5]
my_list[-4:-1]

# Changing the items
fruits = ['banana','apple','mango','melon']
print(fruits)
fruits[1] = 'pears'
print(fruits)

# Adding new elements to a list
fruits = ['banana','apple','mango','melon']
fruits.append('kiwi')
fruits.append(234)
fruits.append(['grapes',90])
print(fruits)

# count items
fruits = ['banana','apple','mango','melon','mango']
fruits.count('mango')

# remove specific items
fruits = ['banana','apple','mango','melon']
fruits.remove('mango')
print(fruits)

# reverse the list
fruits = ['banana','apple','mango','melon']
fruits.reverse()
print(fruits)

# delete last element
fruits = ['banana','apple','mango','melon']
fruits.pop()
print(fruits)

# delete all elements
fruits = ['banana','apple','mango','melon']
fruits.clear()
print(fruits)

# find the index of element
fruits = ['banana','apple','mango','melon']
fruits.index('apple')