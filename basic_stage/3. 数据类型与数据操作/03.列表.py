"""
1.列表基础：
    列表的作用：一次性存储多个数据
    列表的格式：[数据1,数据2,数据3，......]（一个列表）
    列表可以嵌套列表
        使用 Ist[i][j] 表达即可定位到某个具体数据
2.列表操作：
    ①查询：
        index()：查找数据返回下标,若不存在则会报错
        count()：查找数据出现次数
        len():统计列表中数据个数

    ②判断数据是否存在:
        要判断的数据" in 序列，在则返回true，不在返回false

    ③增加数据:
        append() - 列表序列.append(数据)
            使用append函数默认增加数据到列表末尾
            可以追加列表数据到原列表中
        extend() - 列表序列.extend(数据)
            使用extend函数会将数据拆开逐一增加到列表中
        insert() - 列表序列.insert(位置下标,数据)
            指定位置增加数据

    ④删除数据：
        del  - 可以使用del删除列表中指定下标的数据，也可以直接删除整个列表
            语法： del 要删除的目标
        pop() -- 删除指定位置下标的数据，如果不指定下标，默认删除最后一个数据
            可以定义一个新的变量来接收被pop函数删除的数据
        remove(数据) -- 删除列表中想要删除的内容
            语法： list.remove(想要删除的内容)
        clear() -- 清空列表

    ⑤修改数据：修改指定下标数据，然后直接赋值即可

    ⑥列表排序：
        sort(self, key, reverse)
        sort排序中默认升序排列,即默认 reverse = False
            降序排列，将reverse值改为True
        key关键字高级用法：
            列表数据按字典的key排序：
                列表.sort(key=lambda x:x['key'],reverse=bool)

    ⑦复制列表：copy()


3.列表的循环遍历：当出现某种情况需要遍历列表所有数据时，可以使用for循环
    for i in Ist:
        要执行的代码

"""
# 列表查询操作测试
name_list1 = ["TOM", "lzp", "lebron", "lzp"]  # 下标从0开始
print(name_list1[1])  # lzp
print(name_list1.index("lzp"))  # 1
print(name_list1.count("lzp"))  # 2
print(len(name_list1))  # 4

# 列表判断操作测试
print("lzp" in name_list1)  # True

# 体验案例：判断用户输入的数据是否存在
name = input("请输入您的名字：")
if name in name_list1:
    print(f"您输入的名字{name}已经存在")
else:
    print(f"您输入的名字{name}不存在")
print("-" * 10)

# 增加数据测试
name_list2 = ["TOM", "lzp"]
name_list2.append([11, 22])
print(name_list2)  # ['TOM', 'lzp', [11, 22]]
name_list2.extend('zp')
print(name_list2)  # ['TOM', 'lzp', [11, 22], 'z', 'p']
name_list2.insert(1, "a")
print(name_list2)  # ['TOM', 'a', 'lzp', [11, 22], 'z', 'p']

# 删除数据测试
del name_list2[1]
print(name_list2)  # ['TOM', 'lzp', [11, 22], 'z', 'p']
del_name_list2 = name_list2.pop(1)
print(name_list2)  # ['TOM', [11, 22], 'z', 'p']
print(del_name_list2)  # lzp
name_list2.append(2)
print(name_list2)  # ['TOM', [11, 22], 'z', 'p', 2]
name_list2.remove(2)
print(name_list2)  # ['TOM', [11, 22], 'z', 'p']

# 修改数据测试
name_list3 = [1, 5, 6, 9, 8, 5, 2]
name_list3[0] = 8
print(name_list3)  # [8, 5, 6, 9, 8, 5, 2]

# 列表排序测试
list1 = [1, 5, 6, 9, 8, 5, 2]
list2 = ['a', 'b', 'w', 'a', 'k', 'z', 't']

list1.sort(reverse=True)
list2.sort()
print(list1)  # [9, 8, 6, 5, 5, 2, 1]
print(list2)  # ['a', 'a', 'b', 'k', 't', 'w', 'z']

