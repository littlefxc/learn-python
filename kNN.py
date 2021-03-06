#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
import operator
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


def classif0(inX, dataSet, labels, k):
    # 计算距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 降序排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createDataSet():
    # 数据集
    group = array([[1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0.1]])
    # 标签
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


## 1 : 执行 classif0
# group, labels = createDataSet()
# result = classif0([0, 0], group, labels, 3)
# print(result) # B


## 2 : 执行 file2matrix(filename)
# datingTestSet2.txt 中数据意义分别是
# (每年获得的飞行常客里程数，玩视频游戏游戏所耗时间时间百分比，每周消费的冰淇凌公升数，(1:不喜欢的人，2：魅力一般的人，3：极具魅力的人))
datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
print(datingLabels[0:20])

# 散点图使用 datingDataMat 矩阵的第二、第三列数据，分别表示特征值"玩视频游戏所耗时间百分比"和"每周所消耗的冰淇淋公升数"
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.title(u"带有样本类别标签的约会数据散点图", fontproperties=font())
plt.xlabel(u"玩视频游戏所耗时间百分比", fontproperties=font())
plt.ylabel(u"每周所消耗的冰淇淋公升数", fontproperties=font())
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.xlabel(u"玩视频游戏游戏所耗时间时间百分比", fontproperties=font())
plt.ylabel(u"每周消费的冰淇凌公升数", fontproperties=font())
ax1.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()

fig = plt.figure()
ax2 = fig.add_subplot(111)
plt.xlabel(u"每年获得的飞行常客里程数", fontproperties=font())
plt.ylabel(u"玩视频游戏游戏所耗时间时间百分比", fontproperties=font())
ax2.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
