"""
函数就是将一段具有独立功能的代码块整合到一个整体并命名
    在需要而定位置调用这个名称即可，可以更高效的实现代码重用
一、函数基础
    1.定义函数：
        def 函数名(形式参数)：
            代码1
            代码2
            ......
    2.调用函数
        函数名（实参）
    3.函数的返回值：return - 返回return后面的值,需要定义新的变量来接收返回值
        遇到 return 后会退出当前函数，不会执行 return 下方的代码
        return 可以返回元组，返回列表以及返回字典等数据类型，即一个函数有多个返回值的写法可以使用返回列表等数据类型的方法

    实现需求：
        1)计算第一个数×第二个数的乘方
        2) 计算三个数的平均值

    4.变量作用域 - 变量生效的范围：
        局部变量 - 只在函数体内部生效，函数调用完成后，销毁局部变量
        全局变量 - 函数体内外都能生效的变量
        如果想在函数体中修改全局变量，要使用 global关键字声明a为全局变量

    5.函数的参数
        5.1 位置参数 - 根据函数定义的参数位置来传递参数
        5.2 关键字参数 - 通过 “键=值” 的形式加以指定,不分先后顺序
                注意：位置参数要写在关键字参数之前
        5.3 缺省（默认）参数 - 为形式参数设置默认值,写入默认值的参数必须放在最后面
        5.4 不定长参数(可变) - 用于不确定会传递多少个参数
                包裹位置传递 *args - 接收所有位置参数，返回一个元组
                包裹关键字传递 **kwargs - 接收所有关键字参数，返回一个字典

    6.组包与拆包
        6.1组包 - 包裹位置传递和包裹关键字传递本质上就是一个组包的过程
            将零散的数据打包为一个字典或者元组
        6.2拆包和交换变量值
"""


"""函数快速体验"""


# 定义一个函数 add_num1 专门用于计算两个数之和
# 定义函数同时定义接收用户数据的a,b （形式参数）
def add_num1(a, b):
    """
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """  # 定义函数的说明文档
    result = a + b
    print('已经计算完成')
    return result


# 调用函数，如果没有调用函数，那么函数里面的代码不会执行
sum_num = add_num1(10, 20)  # 调用函数中的数据是真实参数，简称实参
print(sum_num)  # 30

help(add_num1)
# 查看函数的解释说明信息
# Help on function add_num1 in module __main__:
#
# add_num1(a, b)
#     求和函数
#     :param a: 参数1
#     :param b: 参数2
#     :return: 返回值


"""函数的嵌套调用："""


# 需求1：计算第一个数×第二个数的乘方
def cf_num2(c):
    result2 = c ** 2
    return result2


def chengfa_num1(a, b):
    b = cf_num2(b)
    result1 = a * b
    return result1


result = chengfa_num1(10, 2)

print(result)  # 40


# 需求2：计算三个数的平均值
def sum1(a, b, c):
    """
    求和函数
    :param a:参数1
    :param b:参数2
    :param c:参数3
    :return:sum1_result(求和结果)
    """
    sum1_result = a + b + c
    return sum1_result


def avg1(a, b, c):
    """
    求平均值
    :param a: 参数1
    :param b: 参数2
    :param c: 参数3
    :return: result2 求平均值后的结果
    """
    result1 = sum1(a, b, c)
    result2 = result1 / 3
    return result2


result = int(avg1(1, 2, 6))
print(result)  # 3

# 测试局部变量与全局变量
a = 100


def test_a():
    b = 101
    print(b)  # 101
    a = 102
    print(a)  # 102


test_a()  # 直接print(b)会报错
print(a)  # 100
# 这里可以看出，a = 102,修改的是函数里面的局部变量a


def test_a2():
    global a
    a = 200


test_a2()
print(a)  # 200
print("-------")


# 测试返回多个返回值
def return_num():
    # return 1, 2  # 返回元组(1, 2)
    return [10, 20, 30]  # 返回列表[10, 20, 30]
    # return {'name': 'zp', 'age': 18}  # 返回字典 {'name': 'zp', 'age': 18}


result = return_num()
print(result)  # 默认返回元组数据类型
print("-------")


# 测试位置参数
def user_info(name, age, gender='man'):
    print(f'您的名字是：{name},您的年龄是：{age},您的性别是：{gender}')


# 位置参数
user_info('lzp', 20, 'man')  # 您的名字是：lzp,您的年龄是：20,您的性别是：man
# 关键字参数
user_info('lzp', gender='man', age=20, )  # 您的名字是：lzp,您的年龄是：20,您的性别是：man
# 缺省参数
user_info('tom', 20)  # 在形式参数中设置默认值，实际传入参数可以省略这个参数
# 您的名字是：tom,您的年龄是：20,您的性别是：man


# 可变参数
def user_info2(*args):
    print(args)


user_info2('TOM')
user_info2("TOM", 20)
user_info2()


def user_info3(**kwargs):
    print(kwargs)


user_info3(name='TOM', age=20)
print("-------")


# 元组拆包 - 变量的个数应该与元组内的个数相等
def return_num2():
    return 1, 2, 3


num1, num2, num3 = return_num2()
print(num1)  # 1
print(num2)  # 2
print(num3)  # 3
# 字典拆包
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1
# 打印key值
print(a, b)
# 打印value值
print(dict1[a], dict1[b])
print('-------')
"""
1.借助第三 变量存储数据（了解即可）
2.简单方法
"""
a = 10
b = 20
# 临时变量c
c = 0
c = a
a = b
b = c
print(a, b, "-----")
# 方法二，简单写法
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)







