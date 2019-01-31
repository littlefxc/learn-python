from numpy import *
import operator

def createDataSet():
    # 数据集
    group = array([[1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0.1]])
    # 标签
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classif0(inX, dataSet, labels, k):
    # 计算距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
result = classif0([0,0], group, labels, 3)
print(result)