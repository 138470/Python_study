"""
for循环语法：
for 临时变量 in 序列：
    重复执行的代码
    .......

for 循环作用：for循环通常用于遍历序列（例如列表、元组、字符串等）或其他可迭代对象
"""
# 演示for循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("-------")

# 使用break 打破循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
print("-------")
# 使用continue 打破循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

#  for与else语句和while 与else 语句类似
#  使用break退出循环时，else后面的的代码不执行
#  使用continue退出循环时，else后面的代码照常执行






