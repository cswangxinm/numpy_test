def plotpic(dataArr, labelArr, wei, b):
    import matplotlib.pyplot as plt
    from scipy import *
    color = ['red', 'blue', 'red']
    m, n = shape(dataArr)
    for i in range(m):
        plt.plot(float(dataArr[i][0]), float(dataArr[i][1]), 'o', 20, color=color[int(labelArr[i])])

    x = arange(-4, 10, 0.1)
    y = (-x*wei[0, 0] - b[0,0])/wei[0, 1]
    plt.axis([-2, 12, -8, 6])
    plt.plot(x, y, color='black')
    plt.show()


