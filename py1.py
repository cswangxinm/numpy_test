'''
@date 3013-6-23

'''

import numpy as np

def pri(*seq):
    '''
    for sequence print
    '''
    for i in seq:
        print(i)


#Crate arrays:
a1 = np.array([0, 1, 2])
a2 = np.arange(3, dtype='i')
a3 = np.arange(3, dtype=np.int32)
a4 = np.r_[0, 1, 2]
a5 = np.concatenate(([0, 1], [2]))
a6 = np.concatenate(([0], [1, 2]))
a7 = np.r_[0:3]
a8 = np.r_[0:2:3j]
a9 = np.array([[2, 3], [5]])
a10 = np.arange(10) #0--9
a11 = np.arange(3,10) #3--9
a12 = np.linspace(1, 10, 3) #[1, 5.5 10]
a13 = np.mgrid[1:2, 3:4] #mgrid=nd_grid(sparse=False)
a14 = np.ogrid[1:2, 3:4] #ogrid=nd_grid(sparse=True)
print('##########')
for i in range(1,15):
    pri(eval('a'+str(i)))


#Type conversion:
b1 = np.int64(np.array([2, 3, 4]))
b2 = np.float32(b1)
b3 = b2.astype(float)
#is a particular type?:
d = np.dtype(int)
b4 = np.issubdtype(d, np.float64)

print(b4)
print('##########')
for i in range(1,5):
    pri(eval('b' + str(i)))


#Convert to common array:
a = np.array([2, 3, 4])
b = a.tolist()

#Special array:
a = np.zeros((2, 3)) # 2-by-3 array
b = np.eye(3)

#indices:
x = np.arange(20).reshape(5, 4)
row, col = np.indices((2, 3))
x[row, col] #equals x[0:2, 0:3] as index

#I/O
from StringIO




