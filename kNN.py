from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(intX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if cmp(listFromLine[3],'didntLike')==0:
           classLabelVector.append(1)
        elif  cmp(listFromLine[3],'smallDoses')==0:
            classLabelVector.append(2)
        elif cmp(listFromLine[3],'largeDoses')==0:
           classLabelVector.append(3)

        index += 1
    return returnMat, classLabelVector

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.radline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


if __name__ == '__main__':
    '''
    test kNN
    '''
    #group, label = createDataSet()
    #curLabel = classify0([0, 0], group, label, 3)

    '''
    test kNN (more datas)
    '''
    #datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    #import matplotlib
    #import matplotlib.pyplot as plt
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    #print array(datingLabels)
    #ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15*array(datingLabels))
    #plt.legend()
    #plt.show()
    '''
    digit recognition
    '''

    pass