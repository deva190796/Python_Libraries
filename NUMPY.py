#importing module
import numpy as np

#creating the arrays

a = np.array([1,2,3])                       #1D array
b = np.array([[1,2,3],[4,5,6]])             #2D array    
c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])   #3D array
d = np.zeros(5, dtype = int)                #with zeros
e = np.ones(5, dtype = int)                 #with ones
f = np.arange(15)                           #range array
g = np.arange(0,11)
h = np.arange(0,11,2)
i = np.linspace(0,5,5)                     #equally spaced
print(a,b,c,d,e,f,g,h,i, sep = "\n")

#array attributes

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)                            #2 rows 3 columns
print(arr.ndim)                             #2D
print(arr.size)                             #6 elements in an array
print(arr.dtype)                            #int64

#array indexing

ind = np.array([10,20,30,40,50])
print(ind[0])                               #10
print(ind[-1])                              #50
print(ind[1:4])                             #[20,30,40]

#2D array indexing and slicing
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat[2,1])
print(mat[:,1])                             #all rows 2nd column
print(mat[1,:])                             #all columns 2nd row

#boolean indexing
bo = np.array([10,20,30,40])
print(bo[bo > 10])

#arithmetic operations
A = np.array([1,2,3])
B = np.array([4,5,6])
print(A + B)
print(A - B)
print(A ** B)

#aggregate functions
agg = np.array([1,2,3,4,5])
print(agg.min())
print(agg.max())
print(agg.mean())
print(agg.sum())
print(agg.std())

#broadcasting
br = np.array([1,2,3])
su = br + 5
print(su)

#reshaping
re = np.arange(12)
print(re.reshape(4,3))
print(re.ravel())
print(re.flatten())

#stacking
st = np.array([1,2,3])
st1 = np.array([4,5,6])
print(np.vstack((st,st1)))
print(np.hstack((st1,st)))

#splitting
sp = np.array([1,2,3,4,5,6])
print(np.split(sp,3))

#Linear algebra
La = np.array([[1,2],[3,4]])
LA = np.array([[5,6],[7,8]])
print(np.linalg.inv(LA))
print(np.dot(La,LA))
print(np.linalg.det(La))
print(np.linalg.eig(LA))

#random module
print(np.random.randint(5))
print(np.random.randint(1,10,5))
print(np.random.randint(1,10,(5,5)))

#transpose
tr = np.array([[1,2,3],[4,5,6]])
print(np.transpose(tr))



