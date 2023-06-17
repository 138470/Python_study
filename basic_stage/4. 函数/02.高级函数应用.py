"""
二、函数的高级应用：
    1.递归
        递归的特点：函数内部自己调用自己，递归必须要有出口
        如果没有出口则报错——超出最大递归深度
        需求：计算10以内的累加和，利用递归实现

    2.lambda表达式
        2.1 lambda表达式(也称匿名函数)的应用场景：一个函数只有一句代码并且只有一个返回值，可以使用lambda简化
        2.2语法：lambda 参数列表：表达式
            lambda的参数：
                1)无参数 - ':'后面直接跟返回值
                    fn1 = lambda: 返回值
                2)一个参数
                    fn1 = lambda a: a 的表达式
                3)缺省参数 - 为参数设置默认值，有实参则用实参，没实参则使用默认值
                    fn1 = lambda a, b, c=100: a+b+c
                4)可变参数 - 不定个数的位置参数
                    *args - 接收不定长的非关键字参数，并返回一个元组
                    **kwargs - 接收不定长的关键字参数，并返回一个字典
        2.3 lambda 的应用：
            带判断的lambda：
                fn1 = lambda a, b:a if a >b else b
                三目运算符：条件成立往前放，不成立往后放
            列表数据按字典的key排序：
                列表.sort(key=lambda x:x['key'],reverse=bool)

    3.高阶函数 - 把一个函数作为另外一个函数的参数来传入：
            abs()函数：对数字进行绝对值计算
            round()函数：对数字的四舍五入计算

            Python中内置的高阶函数：
                map(func, ist) - 把 func 函数作用于 列表 ist 的每个变量中，并返回结果组成新的列表
                    Python3 中会返回一个内存地址，需要使用 list 函数将其转换为列表
                reduce(func, ist) - 把 func 函数的计算的结果作用到 ist序列 的下一个元素
                    使用 reduce 函数必须要导入 functools 模块
                    使用reduce函数中的func函数，必须传入两个参数
                filter(func, ist) - 过滤掉ist列表中不符合条件的元素
                    返回的是一个filter对象，要转换为列表需要使用list()函数
"""


# 体验递归 - 计算数字10以内的累加和
def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)


result = sum_num(10)
print(result)  # 55


# 体验lambda
fn1 = lambda: 100
print(fn1)  # 打印的是内存地址
print(fn1())  # 100,调用函数后才可以打印出返回值

# 多个参数
# 示例：计算 a + b + c
fn2 = lambda a, b, c: a+b+c
print(fn2(1, 2, 3))  # 6

# 缺省参数测试
fn3 = lambda a, b, c=100: a+b+c
print(fn3(1, 2,))  # 103
print(fn3(1, 2, 3))  # 6

# 可变参数测试
fn4 = lambda *args: args
# args这个变量存储的即为用户传入的不定长的数据的元组
# 若要对传入的数据进行计算，要进行元组的遍历，便不能使用lambda表达式
print(fn4(1, 20, 24))  # (1, 20, 24)
fn5 = lambda **kwargs: kwargs
print(fn5(name='lzp', age=18))  # {'name': 'lzp', 'age': 18}


# 列表数据按字典的key排序
students = [{'name': 'zp1', 'age': '18'}, {'name': 'zp2', 'age': '17'}, {'name': 'zp3', 'age': '16'}]
students.sort(key=lambda x: x['name'], reverse=False)
print(students)  # [{'name': 'zp1', 'age': '18'}, {'name': 'zp2', 'age': '17'}, {'name': 'zp3', 'age': '16'}]


# 任意两个数字,先进行数字处理，再求和计算
# 数字处理方式：求绝对值或者四舍五入 (round) 计算
def sum1(a, b, f):
    return f(a) + f(b)


result = sum1(-1.5, 20.4, round)  # 若想对数字进行绝对值处理，改为abs即可
print(result)  # 18

# map()函数应用 - 求列表元素的平方
list1 = [1, 4, 5, 8, 10]


def list_map(x):
    return x ** 2


result = map(list_map, list1)
print(list(result))

# reduce() 函数应用 - 求列表累加
import functools

list2 = [1, 2, 3, 4, 5]


def sum2(a, b):
    return a + b


result = functools.reduce(sum2, list2)
print(result)

# filter函数应用 - 列表取偶数
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_list(x):
    return x % 2 == 0  # 可以理解为过滤条件


result = filter(filter_list, list3)
print(list(result))
