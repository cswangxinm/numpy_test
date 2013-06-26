from scipy import *
from scipy.linalg import *
import matplotlib.pyplot as plt

def plainG(x, y, u, e, D):
    detE = det(e)
    return 1/((2*pi)**(D/2.0)) * 1/(detE**0.5) *exp(-0.5*(mat([x,y]).T - u).T * e.I * (mat([x,y]).T - u))


def cGaussian(x, u, e, D):
    detE = det(e)
    return 1/((2*pi)**(D/2.0)) * 1/(detE**0.5) *exp(-0.5*(x - u).T * e.I * (x - u))

def estep(x, u, e, p_i, N, r):
    for n in range(N):
        total = 0.0
        for i in range(2):
            total += p_i[i] * cGaussian(mat(x[n]).T, u[i], e[i], 2)
        for k in range(2):
            r[n, k] = p_i[k] * cGaussian(mat(x[n]).T, u[k], e[k], 2)/ total

def mstep(x, u, e, p_i, N, r):
    tmp = []
    tmp.append(zeros((2, 1)))
    tmp.append(zeros((2, 1)))
    tmp_nk = [0.0, 0.0]
    for k in range(2):
        for n in range(N):
            tmp_nk[k] += r[n, k]
    for k in range(2):
        for n in range(N):
            tmp[k] += r[n, k] * mat(x[n]).T #for u

    for k in range(2):
        tmpe = mat('0.0 0.0; 0.0 0.0')
        u[k] = tmp[k] / tmp_nk[k]
        for n in range(N):
            tmpe += r[n, k] * (mat(x[n]).T - u[k])*(mat(x[n]).T - u[k]).T
        e[k] = tmpe / tmp_nk[k]
        p_i[k] = tmp_nk[k] / N





def plotGaussian(u, e):
    '''
    a = arange(0, 10, 0.1)
    b = arange(0, 10, 0.1)
    for i in a:
        for j in b:
            plainG(x, y, u[0], e[0], 2)[0,0]
    plt.contour(x, y, , inline=1)
    #plt.show()
    '''

fp = open('readfile.txt')
x = []
for i in fp.readlines():
    a, b = i.split(' ')
    x.append([float(a), float(b)])

N = len(x)
u = []
u.append(zeros((2, 1)))
u.append(ones((2, 1)))
e = []
e.append(mat(eye(2)))
e.append(mat('2.0 0.0; 0.0, 2.0'))
p_i = [0.5, 0.5]

r = zeros((N, 2))

if __name__ == '__main__':

    for i in range(100):
        estep(x, u, e, p_i, N, r)
        mstep(x, u, e, p_i, N, r)


    print u


    #plotGaussian(u, e)
    plt.axis([-10, 10, -10, 10])
    for i in range(N):
        plt.plot(x[i][0], x[i][1], 'o')
    plt.show()

