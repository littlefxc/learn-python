#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


# python 的面向对象的概念可以从 Java 中很好的过渡过去
# 使用方式：
# import sys;
# sys.path.extend(['/Users/fengxuechao/PycharmProjects/learn-python'])
# from learn_python_class import Student
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()