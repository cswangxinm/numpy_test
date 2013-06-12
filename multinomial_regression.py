from numpy.linalg import *
from scipy import *
import matplotlib.pyplot as plt

x = arange(0, 2, 0.1);
t = 5*x**3 + 2*x**2 + 3
t += random.randn(1, 20).flatten()*2

for i in t:
    print i

#optimization:
w = zeros(4, dtype='f8')
X = ones(4, dtype='f8')
alpha = 0.001
w1 = 100.0
wtmp = 0.0
e = 100
w_tmp = zeros(4, dtype='f8')

while e  > 80:
    e = 0
    w_tmp.fill(0.0)

    for i in arange(0, 2, 0.1):
        X[0] = 1
        X[1] = i
        X[2] = i**2
        X[3] = i**3
        w_tmp += ((w.dot(X)-t[int(i*10)])*X)

    w -= w_tmp*alpha

    for i in arange(0, 2, 0.1):
        X[0] = 1
        X[1] = i
        X[2] = i**2
        X[3] = i**3
        e += (w.dot(X)-t[int(i*10)])**2

    print e

print ('e', e)

#plot
z = arange(0, 2, 0.1);

for i in arange(0, 2, 0.1):
    X[0] = 1
    X[1] = i
    X[2] = i**2
    X[3] = i**3
    z[int(i*10)] = w.dot(X)

print z
plt.plot(x, t, 'o', x, z, '-')
plt.show()