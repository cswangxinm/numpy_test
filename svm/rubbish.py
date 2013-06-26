import numpy.random as r

s = r.normal(5, 1, 100)


m = len(s)
for i in range(m/2):
    print s[i*2], s[i*2+1]