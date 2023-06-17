# 集合（set）是一种无序的数据结构，它不会保留元素的插入顺序。
# 集合与字典相似，里面的数据是不允许重复的，当出现重复数据时，默认删除后面重复的数据
s1 = {10, 20, 30, 40, 50, 10}
print(s1)
# 创建一个空集合只能使用set()
s2 = set()  # 使用s2 = {}创建的是空字典
print(type(s2))
print("----------")
"""
集合是可变的数据类型
集合的常见操作方法：
    1.增加数据：
        add() - 增加单一数据
        update() - 增加的数据是序列
    2.删除数据：
        remove() - 删除集合中指定的数据
        discard() - 同上，删除指定数据
        pop() - 随即删除某个数据，并返回这个数据
    3.查找数据：
        in:判断数据在集合序列
        not in :判断数据不在集合序列
    
"""
s3 = {10, 20}
s3.add(30)  # 使用add()添加序列时会报错
print(s3)
s3.update([60, 40, 50])  # 使用update()时如果增加单一数据会报错
print(s3)

s3.remove(60)  # remove 和discard的区别在于，如果删除的数据不存在，remove会报错，discard不会
print(s3)

s3_pop = s3.pop()
print(s3_pop)
print(s3)

print(40 in s3)
print(40 not in s3)


