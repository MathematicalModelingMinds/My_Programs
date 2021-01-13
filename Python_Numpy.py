# Define arrays
import numpy as np
a = [2,4,6,8]
print(a)
type(a)

b = np.array(a)
print(b)
type(b)

c = np.array([1, 2, 3]) 
print(c)
type(c)

d = np.array([[1,2,3],[4,5,6]])
print(d)
type(d)

# arange function
e = np.arange(0,10)
print(e)
type(e)

e = np.arange(0,10,2)
print(e)

# zeros function
f = np.zeros((5,4))
print(f)

# Ones function
g = np.ones((2,8))
print(g)

# Linearly spaced numbers
np.linspace(0,10,6)
np.linspace(0,10,20)

# Random integers
np.random.randint(0,100)

#Random arrays
np.random.randint(0,100,(4,4))

# Array operations
np.random.seed(100)
x = np.random.randint(0,100,20)
print(x)
x.max()
x.min()
x.mean()
x.argmax()
x.argmin()

y = x.reshape(4,5)
print(y)
y[3,2]
y[:,2]
y[3,:]

# Shape of the array
print(y.shape)

# Conditional filters
np.random.seed(101)
z = np.random.randint(0,100,50).reshape(5,10)
print(z)

z<40

z[z<40]

# Matrix operations
import numpy as np
mat1 = np.array([[1, 2], [3, 4]])
print(mat1)

# Transpose of mat1
mat1.transpose()

# Dot product of 2 matrices
mat2 = np.array([[5, 6], [7, 8]])
mat1 @ mat2 

# Inverse of a square matrix
np.linalg.inv(mat1)

# Trace 
np.trace(mat1)

# Identity matrix
np.eye(3)

