"""
字典的概念：
    字典是以键值对的形式存储数据的，即 key:value
    key是唯一的
字典的操作：
    创建一个新的字典：如果存在重复的key，则默认保存后面key所对应的值
    增加/修改数据：
        直接赋值即可。如果字典中存在键则修改其对应的值,如果不存在，则新增键
    删除数据：
        del 想要删除的某个key或者删除整个字典
            没有这个键值对的话会报错
        dic.clear() 清空所有键值对
    查找：
        1.get() - 查找某个key对应的值
            语法：字典序列.get(key, 默认值)
            查找的key存在对应的值，不存在返回默认值

        2.keys() - 查找字典中所有的key
            语法：字典序列.keys()

        3.values() - 查找字典中所有的值
            语法：字典序列.values()

        4.items()
            作用：查找字典中所有的键值对，返回一个可迭代的对象（注意：不是列表）
                列表数据是存储每个键值对的元组，元组数据1为key，元组数据2为值
            语法：字典序列.items()
    字典的遍历：for循环
        遍历 key
        for i in dict2.keys():
        遍历字典的值
        for j in dict2.values():
        遍历所有键值对,并对键值对进行拆包
        for j in dict2.items():
       元组中有两个数据，所以可以定义两个临时变量对其进行拆包
        for key, value in dict2.items():
            print(f'{key} ... {value}')
"""
# 创建一个有数据的字典——字典是以键值对的形式出现的
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'man', 'name':'zp'}
print(dict1)  # {'name': 'zp', 'age': 20, 'gender': 'man'}
dict1["id"] = 110
print(dict1)  # {'name': 'zp', 'age': 20, 'gender': 'man', 'id': 110}
dict1['name'] = 'lzp'
print(dict1)  # {'name': 'lzp', 'age': 20, 'gender': 'man', 'id': 110}

# 使用del删除字典或者某个键值对,如果没有这个键值对会报错
del dict1['gender']
print(dict1)  # {'name': 'lzp', 'age': 20, 'id': 110}

dict1.clear()
print(dict1)  # {}
print("---------")


# key值查找
dict2 = {'name': 'Tom', 'age': 20, 'gender': 'man'}
print(dict2['name'])  # Tom,key不存在会报错
print(dict2.get('names', 200))  # 200,不设置默认值时返回none
print(dict2.keys())  # dict_keys(['name', 'age', 'gender'])
print(dict2.values())  # dict_values(['Tom', 20, 'man'])
print(dict2.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', 'man')])

print("---------")

# 字典的循环遍历
# 遍历字典的key
for i in dict2.keys():
    print(i, end=" ")  # name age gender
print()
# 遍历字典的值
for j in dict2.values():
    print(j, end=" ")  # Tom 20 man
print()
# 遍历所有键值对,并对键值对进行拆包
for j in dict2.items():
    print(j, end=" ")  # ('name', 'Tom') ('age', 20) ('gender', 'man')
print()
# 元组中有两个数据，所以可以定义两个临时变量对其进行拆包
for key, value in dict2.items():
    print(f'（键为{key} ，值为{value}）', end=', ')

