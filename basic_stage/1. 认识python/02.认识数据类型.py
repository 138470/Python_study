# 使用id()关键字测试可变数据类型与不可变数据类型
# id() - 可以返回变量的十进制内存地址
a = 1  # 计算机开辟一个内存地址，名为a，a即为引用，可以粗暴的理解为变量名
b = a  # 将这个地址的名字由a改为b,但是这个内存地址存的依然是1
print(id(a))
print(id(b))  # a与b的地址一样，即a与b引用了同一个对象
c = 1
print(id(c))  # c的地址与ab一样说明python中的值是靠引用来传递的

# 测试不可变数据类型
a = 2
print(id(a))  # 更改a所对应的数据，a所引用的对象也发生了改变

# 测试可变数据类型
aa = [10, 20, 30]
bb = aa
aa.append(30)
print(bb)  # 更改aa的值后，bb的值也做了修改。说明aa,bb是同一个数据的引用
print(id(aa), id(bb))  # 更改aa的值后两个引用依然指向同一个对象，这就是可变数据类型

print("-------")

# 整型int - 整型属于不可变的数据类型
a = 1
print(type(a))

# 浮点型float
b = 1.1
print(type(b))

# 布尔型bool 两个取值，true or false
c = True
print(type(c))

# 字符串类型str，数据都要带引号
d = "abc"
print(type(d))

# 列表list
e = [10, 20, 30]
print(type(e))

# 元组tuple
f = (10, 20, 30)
print(type(f))

# 集合set
g = {10, 20, 30}
print(type(g))

# 字典dict--键值对
h = {"name": "abc", "age": 18}
print(type(h))


