from numpy import *
import operator

def createDataSet():
    # 数据集
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # 标签
    labels = ['A', 'A', 'B', 'B']
    return group, labels
