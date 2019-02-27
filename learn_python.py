# 输出

# 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。
import functools

print('hello, world')

# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

# print()也可以打印整数，或者计算结果:
print(300)
print('100 + 200 =', 100 + 200)

# 输入

# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字：
print("请输入用户名：")
name = input()
print('name =', name)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


# 列表生成式
L = [x * x for x in range(10)]
print("列表生成式：[x * x for x in range(10)] =", L)
g = (x * x for x in range(10))
print("列表生成式改造成生成器，只要把一个列表生成式的[]改成()，就创建了一个generator：\n(x * x for x in range(10)) =", g)
for g_val in g:
    print(g_val)


# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def generate_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 高阶函数 sorted()
print("Python内置的sorted()函数就可以对list进行排序："
      "sorted([36, 5, -12, 9, -21]) =", sorted([36, 5, -12, 9, -21]))
print("sorted()函数也是一个高阶函数，"
      "它还可以接收一个key函数来实现自定义的排序，"
      "例如按绝对值大小排序："
      "sorted([36, 5, -12, 9, -21], key=abs)=", sorted([36, 5, -12, 9, -21], key=abs))
print("忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写）,再比较:"
      "sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) = ",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


# 装饰器:在代码运行期间动态增加功能的方式
print("装饰器:在代码运行期间动态增加功能的方式")


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_parameter(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print("2019-02-27")


def yesterday():
    print("2019-02-26")


now()
yesterday = log(yesterday)
yesterday()

