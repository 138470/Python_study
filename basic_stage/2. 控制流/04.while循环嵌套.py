"""
惹了老婆生气，老婆让你说三遍“媳妇我错了”
然后惩罚你刷晚上的碗。
上述惩罚连续执行三天。

嵌套循环语法：
while 条件1：
    条件1成立执行的代码
    ......
    while 条件2:
        条件2成立执行的代码
        ......
"""

j = 0
while j < 3:
    i = 0
    while i < 3:
        print("媳妇我错了")
        i += 1
    print("晚上我刷碗")
    print("-------")
    j += 1
#  子循环执行完了后再执行下一次的父循环

#  while循环嵌套应用1：打印正方形星号
j = 0
while j < 5:
    i = 0
    while i < 5:
        print("* ", end="")  # 取消\n结束换行
        i += 1
    print()
    j += 1
print("-------")
#  while循环嵌套应用2：打印三角形星号
j = 0
while j < 5:
    i = 0
    while i <= j:
        print("* ", end="")  # 取消\n结束换行
        i += 1
    print()
    j += 1
print("-------")
#  while循环嵌套应用3：九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f"{i}X{j}={j*i}", end="\t")  # \t制表位自动对齐
        i += 1
    print()
    j += 1

