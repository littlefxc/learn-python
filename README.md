---
title: Python 学习记录
date: 2019-02-28 19:46:00
tags:
- Python
---

# Python 学习记录

## 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。

但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

例如：

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```

> 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

## 递归

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

## 切片

```python
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
```

`L[0:3]` 表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

## Python代码的格式

```python
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()
```