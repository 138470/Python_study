"""
公共运算符：
    1. + - 合并，适用于字符串、列表、元组
    2. * - 复制，适用于字符串、列表、元组
    3.in/not in - 判断元素是否存在
        适用于字符串、元组、列表、字典
"""
# 加号运算符，乘号运算符
# 除了三种类型外，其他的数据使用合并运算符会报错
str1 = 'aa'
str2 = 'bb'
print(str1 + str2)  # aabb
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # [1, 2, 3, 4]
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# in/ not in
print('a' in str1)  # True
print('5' in list1)  # False

dict1 = {'name': 'lzp', 'sex': 'men'}
print('name' in dict1.keys())  # True
print("-" * 10)  # 复制十份

"""
公共方法：
    1.len() - 计算容器中元素的个数
    2.del/ del() - 删除功能
    3.max()/ min() -返回容器中最大值/最小值
    4.range(start, end, step) 
        生成从start到end的数字，步长为step，返回一个可迭代的对象
    5.enumerate(可遍历的对象，start = 0) - 返回一个可迭代的对象
        start用来设置遍历数据的下标起始值
"""
str3 = 'abcedfg'
list3 = [1, 2, 3, 4, 5, 6, 7]
t3 = (1, 2, 3, 4, 5)
s1 = {10, 20, 30, 40, 50}
dict1 = {'name': 'tom', 'age': 18}

print(max(list3))  # 7
print(min(str3))  # a

for i in range(1, 10):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9
print()
for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9
# 结果不包含结束位置的数字
# 不写步长默认为1
# 不写开始位置，默认从0开始
print()
print('-'*10)

# enumerate()函数
list2 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list2, start=0):
    print(i, end=" ")  # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
print()
for i in enumerate(list2, start=1):
    print(i, end=" ")  # (1, 'a') (2, 'b') (3, 'c') (4, 'd') (5, 'e')
print()
print("-" * 10)
"""
列表推导式：用一个表达式创建一个有规律的列表或控制一个有规律的列表
"""
# 需求1：创建一个包含0-9的列表
list1 = [i for i in range(10)]
# 列表推导式读取写都从for循环开始，返回值填在左边
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 需求2：创建一个0-10的偶数列表
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)  # [0, 2, 4, 6, 8]

# 需求3：创建列表如下：[(1,0),(1,1),(1,2),(2,0)(2,1)(2,2)]
list3 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list3)  # 多个for循环实现列表推导式等于循环嵌套
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print("-"*10)

"""
字典推导式 - 快速合并列表为字典,或者提取字典中的目标是数据
"""
# 需求1：创建字典 - key是数字1-5，value为数字的平方
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 需求2：将两个列表和并为一个字典
list4 = ['name', 'age', 'gender', 'id']
list5 = ['lzp', '20', 'man']
dict2 = {list4[i]: list5[i] for i in range(len(list5))}
print(dict2)  # {'name': 'lzp', 'age': '20', 'gender': 'man'}
# 如果两个列表数据个数相同，len()任何一个都可以
# 如果两个列表数据个数不同，len()统计个数少的列表

# 需求3：提取字典中的目标数据
# 提取下列电脑数量大于200的电脑数据
counts = {'mbp': 268, 'del': 201, 'hp': 125, 'lenovo': 199, 'acer': 99 }
dict3 = {key: value for key, value in counts.items() if value >= 200}
print(dict3)  # {'mbp': 268, 'del': 201}


"""
集合推导式
"""
# 需求：创建一个集合，数据为下方列表的2次方
list6 = [1, 1, 2]
set1 = {i**2 for i in list6}
print(set1)  # {1, 4}
