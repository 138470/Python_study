"""
input输入的特点:
    1.等待用户输入完成后才执行下一条命令
    2.要定义一个变量来接收用户输入的数据
    3.输入的任意的数据都当作字符串来处理，要进行数据类型转换

数据类型转换：要转换什么类型，就用什么类型的函数
    例如：转换为整形 :int(a)
"""
password = input("请您输入密码：")
print(f"您输入的密码为{password}")
print(f'{type(password)}\n-------')

# 将用户输入的数据转换为其他数据类型
# 转换为整型
print(type(int(password)))

num1 = 1
str1 = "10"

# 数据类型转换
# 1.float(),将数据转换为浮点型
print(type(float(num1)))
print(float(num1))
print(float(str1))

# 2.str(),将数据转换为字符型
print(type(str(num1)))

# 3.tuple(),将一个序列转换为元组
list1 = [10,  20, 30]
print(tuple(list1))

# 4.list()，将一个序列转换为列表
tuple1 = (10, 20, 30)
print(list(tuple1))

# 5.eval(),将字符串转为数据原本的格式
str2 = "1.0"
str3 = "(10, 20, 30)"
str4 = "[10, 20, 30]"

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))










