
def plotLine(weight):
    import matplotlib.pyplot as plt
    from scipy import *
    fp = open('testSet.txt')

    fig = plt.figure()
    fig.add_subplot(111)
    plt.axis([-4, 4, -5, 20])

    L = []
    color = ['blue', 'red']
    for i in fp:
        L = i.strip().split('\t')
        plt.plot(float(L[0]), float(L[1]), 'o', 10, color=color[int(L[-1])])

    x = arange(-3, 3, 0.1)


    try:
        y = (-weight[0, 0] - weight[1, 0]*x)/weight[2, 0]
    except:
        y = (-weight[0] - weight[1]*x)/weight[2]


    plt.plot(x, y)
    plt.show()