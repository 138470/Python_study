""""
1.准备数据
2.格式化符号输出
    整数格式输出 ：
        - 直接输出某个整数，直接用 f 语句
        - %0xd ——x表示输出的整数显示位数，不足的以0补全，超过的以原样输出
    浮点型格式输出 ：
        - 直接输出浮点型数据默认保留六位小数
        - %.xf x表示你要保留的小数位数 如：%2f-保留两位小数
    字符串格式输出 ：
        - 当输出的字符串中有特殊符号时，如'',要加转义符\,否则会报错
        - 字符串切片操作等详见11
3.多个格式化输出，照猫画虎即可
4.print语句：
    使用end来控制 print 以何种方式结束输出
    \n 换行符，print默认换行
    \t 制表符，带有对齐功能

"""
age = 18
weight = 70.5
stu_id = 1
stu_id2 = 182100530
name = "lzp"

# 1. 整数格式输出：
# 1.1今年我的年龄是x岁
# print("今年我的年龄是%d岁" % age)
print(f'今年我的年龄是{age}岁')  # 直接输出某个整数时使用f即可
# 1.2 我的学号是x
# print("我的学号是%d" % stu_id)

# 整数的格式输出
print("我的学号是%03d" % stu_id)
print("我的学号是%03d" % stu_id2)
print(f"我的学号是%03d" % stu_id2)

print("-------")

# 2. 浮点型格式输出：我的体重是x公斤
print("我的体重是%f公斤" % weight)
print("我的体重是%.2f公斤" % weight)
print('-------')

# 3. 字符串型格式输出：我的姓名是x
# print("我的姓名是%s" % name)
print(f"我的姓名是{name}")  # 直接输出字符串用f即可
a = "他说：\" i love u\""
print(a)
print('-------')

# 4. 我的姓名是x，今年x岁了,明年x岁了
print("我的姓名是%s，今年%d岁了" % (name, age))
print("我的姓名是%s，明年%d岁了" % (name, age + 1))
print(f"我的姓名是{name}，今年{age}岁了,明年{age + 1}岁了")

# 5. 我的名字是x，今年x岁了，学号是x，体重是x公斤
print("我的名字是%s，今年%d岁了，学号是%d，体重是%.1f公斤" % (name, age, stu_id, weight))
print("我的名字是%s，\n今年%s岁了，\t\t学号是%03d，体重是%s公斤" % (name, age, stu_id, weight))

# 6. print结束符
print("hello python", end="\n")
print("hello python", end="...")
print("hello python", end="\t\t")
print(age, "hello python", end="\tover")
