# k-近邻算法(kNN) - 学习记录

## 概述

优点：精度高、对异常值不敏感、无数据输入假定。

缺点：计算复杂度高、空间复杂度高。

适用数据范围：数值型和标称型。

### 工作原理：

存在一个样本数据集合，也称训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一数据与所属分类的对应关系。输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本集中特征最相似（最近邻）的分类标签。一般来说，我们只选择样本数据集前 k 个最相似的数据（这就是k-近邻算法中 k 的出处），通常 k 是不大于 20 的整数。最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。

### k-近邻算法的一般流程

1. 收集数据：可以使用任何方法。
2. 准备数据：距离计算所需要的数值，最好是结构化的数据格式。
3. 分析数据：可以使用任何方法
4. 训练算法：此步骤不适用与k-近邻算法
5. 测试算法：计算错误率
6. 使用算法：首先需要输入样本数据和结构化的输出结果，然后运行k-近邻算法判定输入数据分别属于哪个分类，最后应用对计算出的分类执行后续的处理。

### k-近邻算法：伪代码

对未知类别属性的数据集中的每个点一次执行以下操作：

1. 计算已知类别数据集中与当前点之间的距离；
2. 按照距离递增次序排序；
3. 选取与当前点距离最小的 k 个点；
4. 确定前 k 个点所在类别的出现频率
5. 返回前 k 个点出现频率最高的类别作为当前点的预测分类

### k-近邻算法：python3 实现

```python
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
    # 降序排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
```

### 示例1：改进约会网站的配对效果

标签：

- 不喜欢的人
- 魅力一般的人
- 极具魅力的人

特征：

- 每年获得的飞行常客里程数
- 玩视频游戏所耗时间百分比
- 每周消费的冰淇淋公升数




## 参考书：

《机器学习实战》 第二章 k-近邻算法


