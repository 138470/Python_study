"""
1.下定义，将剪刀石头布量化
2.将电脑所出的结果划定为某一定值
3.分析可能出现的结果：
① 玩家胜：玩家剪刀（0）电脑布（2）；玩家石头（1）电脑剪刀（0）；玩家布（2）电脑石头（1）
② 平局：玩家所出的结果和电脑一致
③ 电脑胜：不是玩家胜或者平局的情况，剩下的情况即为电脑胜
3.将电脑的结果改为随机数
引入random模块，使用randint方法将电脑的结果变为从0到2的随机数
"""
import random  # 引入random模块
player = int(input("请输入您的结果（剪刀--0；石头--1，布--2）："))
computer = random.randint(0, 2)
print(f"电脑的结果为：{computer}")

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player ==2 and computer == 1):
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")

print("-------")


