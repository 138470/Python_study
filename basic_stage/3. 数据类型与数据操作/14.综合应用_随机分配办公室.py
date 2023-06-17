# 需求：有三个办公室，8位老师，8位老师随机分配到三个办公室
import random
# 准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

for name in teachers:  # 遍历列表取得数据
    num = random.randint(0, 2)  # 定义一个随机数
    offices[num].append(name)  # 遍历到谁就追加到谁

print(offices)

# 增加需求，显示格式为，办公室X的人数为：X,老师分别是：X,X,X
i = 1
for office in offices:
    print(f"办公室{i}的人数为：{len(office)},老师分别是：")
    for name in office:
        print(name)
    i += 1
