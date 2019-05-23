"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 冯雪超
"""

print('hello, world!')
# print("你好,世界！")
print('你好', '世界')
# sep: 分隔符; end: 结尾字符串
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')

import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()