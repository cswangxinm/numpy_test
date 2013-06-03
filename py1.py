'''
contains:
1. create arrays
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

print('##########')
for i in range(1,9):
    pri(eval('a'+str(i)))


#Type conversion:
b1 = np.int64(np.array([2, 3, 4]))
b2 = np.float32(b1)
b3 = b2.astype(float)

print('##########')
for i in range(1,4):
    pri(eval('b' + str(i)))


