"""
元组与列表的区别：
元组可以存储多个数据，但是元组数据是不可修改的
所以元组的操作只支持查找
"""
t1 = (10, 20, 30)  # 定义多个数据的元组
t2 = (10,)  # 定义单个数据元组必须要有,
t3 = (10)  # 不加,的话括号里面是什么数据类型t3就是什么数据类型
print(t1)
print(type(t2))
print(type(t3))
# 元组操作
tuple1 = ("aa", "bb", "cc", ["li", "haha"])
# 1.下标
print(tuple1[0])
# 2.index()
print(tuple1.index("aa"))  # 没有检索结果会报错
# 3.count()
print(tuple1.count("aa"))
# 4.len()
print(len(tuple1))

# tuple1[0] = aaa 修改元组数据会报错
# 元组里面如果有列表，可以修改列表里面的数据
tuple1[3][0] = "lzp"
print(tuple1)
