"""
while 语句语法：
while 条件：
    条件成立后重复执行的代码1
    条件成立后重复执行的代码2
    .......

else 与 while 配合语法：
while 条件：
    条件成功后执行的代码1
    条件成功后执行的代码2
    .......
else:
    退出循环后执行的代码

退出循环的方式:break，continue
    break  - 直接退出循环，属于非正常退出，else后面的代码不执行
    continue - 退出当前循环，注意要改变 i 的值（退出循环前i+1），完成循环后继续执行else后面的代码

"""
# 快速体验
i = 0  # 计数器一般从0开始
while i < 2:  # 循环几次就小于几
    print("媳妇我错了")
    i += 1  # i=i+1
print("-------")

# 应用1：1-100数字累加
i = 0
a = 0
result = 0
while i < 100:
    i = i + 1  # i控制循环次数,从0开始循环100次
    a = a+1  # a为自增变量
    result = result + a  # 实现累加效果
print(result)

# 应用2：1-100偶数累加和
i = 2
sum1 = 0
while i <= 100:
    sum1 = sum1 + i
    i += 2
print(sum1)  # 这种方法更倾向于人脑计算，不建议

# 应用2另一种方法：除余累加
i = 1
sum1 = 0
while i <= 100:  # i遍历1-100所有数字
    if i % 2 == 0:
        sum1 = sum1 + i  # 控制只累加偶数
    i += 1
print(sum1)  # 这种方法更倾向于让计算机判断是否为偶数，建议使用

print("-------")

#  退出循环的方式：break（终止整个循环） ，continue（退出当前循环）
i = 1
while i <= 5:
    print(f"吃了第{i}个苹果")
    if i == 3:
        print("吃饱了，不吃了")
        break
    i += 1
print("-------")

i = 1
while i <= 5:

    if i == 3:
        print("有虫子，不吃了")
        i += 1  # 使用continue语句如果不使变量加1，则会使i=3一直循环
        continue

    print(f"吃了第{i}个苹果")
    i += 1
print("-------")

# 使用break退出循环时说明循环是非正常结束的，else下方的代码是不执行的
i = 1
while i <= 5:
    print("雷猴啊")
    if i == 2:
        print("从这里结束")
        break
    i += 1
else:
    print("雷猴雷猴")
print("-------")

# 使用continue退出循环时，循环完整进行了，else后面的语句照常执行
i = 1
while i <= 5:
    if i == 3:
        print("从这里结束")
        i += 1
        continue
    print("雷猴啊")
    i += 1
else:
    print("雷猴雷猴")