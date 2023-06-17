"""
基于类的面向对象编程（OOP）：
    当解决一个问题的时候，面向对象会把事物抽象成对象的概念
    就是说这个问题里面有哪些对象，然后给对象赋一些属性和方法，然后让每个对象去执行自己的方法

类：
    可以理解为创建对象的图纸
    用类创建对象，一个类可以创建多个对象
    类是抽象的
对象/实例：
    由类创建出来的一个具体存在
    实例可以使用类中定义的属性和方法，也可以拥有自己的属性和方法。

属性与方法：
    属性用以描述对象的特征
    方法则是定义在类中的函数

    魔法方法：
        __init__(self, 参数1, 参数2, ...):
            设置初始化属性, __init__方法是默认被调用的方法，不需要手动调用
        __str__():
            return '解释说明类的文字'
         __del__():
            删除对象，自动调用
"""


# 定义一个洗衣机类
class Washing_machine:  # 命名类名要遵循大驼峰命名习惯
    # 为类设置一个属性
    weight = 100

    def __init__(self, height, width):
        self.height = height
        self.width = width
        print('start')

    def wash(self):
        # self是指实例对象，根据类创建haier1对象就代表haier1
        # 创建haier2对象就指的是haier2
        print('洗衣服')
        print(self.height)

    def __str__(self):
        return '这是洗衣机的说明书'
        # 通常会返回一些解释说明的文字

    def __del__(self):
        print('对象已经删除')


# 根据洗衣机类创建对象
# 因为定义了带参数的__init__方法，可以传入不同的参数以设置不同对象的默认属性的值
haier1 = Washing_machine(40, 50)  # start
print(haier1.weight)  # 100
haier1.wash()  # 洗衣服  40

# 直接print(haier1)会打印haier1对象的内存地址
# 因为定义了__str__方法,便会直接打印出方法中return返回的值
print(haier1)
del haier1
print('-' * 10)

"""
综合应用：
一、烤地瓜
    需求：用户自己选择烤地瓜的时间和调料
        1.被烤的时间和对应的地瓜状态：
            0-3分钟：生的
            3-5分钟：半生不熟
            5-8分钟：熟的
            超过八分钟：烤糊了
        2.添加的调料：
            用户根据自己的需求添加调料
    分析：
        地瓜的属性：
            被烤的时间
            地瓜的状态
            添加的调料
        地瓜的方法：
            被烤：
                用户根据自己的意愿设置烤地瓜的时间
                判断地瓜被烤的时间修改地瓜的状态
            添加调料：
                用户根据自己的意愿添加调料
                将用户添加的调料存储
                
2.搬家具
    需求：将小于房子剩余面积的家具搬到房子里
    
    
    
"""


# 烤地瓜测试
class Sweet_potato:
    def __init__(self):
        # 定义地瓜初始化属性
        self.coast_time = 0
        self.coast_state = '生的'
        self.flavour = []

    def cook(self, time):
        self.coast_time += time
        if 0 < self.coast_time <= 3:
            self.coast_state = '地瓜是生的'
        elif 3 < self.coast_time <= 5:
            self.coast_state = '地瓜是半生不熟的'
        elif 5 < self.coast_time <= 8:
            self.coast_state = '地瓜是熟的'
        elif self.coast_time > 8:
            self.coast_state = '烤糊了'

    def __str__(self):
        return f'这个地瓜被烤了{self.coast_time}分钟，状态是{self.coast_state},添加过的调料有：{self.flavour}'

    def add_flavor(self, a):
        self.flavour.append(a)


digua1 = Sweet_potato()
print(digua1)
digua1.cook(4)
print(digua1)
digua1.add_flavor('酱油')
digua1.add_flavor('香菜')
print(digua1)
print('-' * 10)


# 搬家具测试
class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.free_area = area
        self.fur_list = []

    def __str__(self):
        return f'您的房子名称为{self.name},房屋面积是{self.area},已经搬入的家具有：{self.fur_list},剩余面积为{self.free_area}'

    def add_fur(self, item):
        if self.free_area > item.area:
            self.fur_list.append(item.name)
            self.free_area = self.free_area - item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')


chair = Furniture('椅子', 5)
desk = Furniture('桌子', 10)
zp_house = House('zp_house', 200)
print(zp_house)
zp_house.add_fur(chair)
zp_house.add_fur(desk)
print(zp_house)
basketball_place = Furniture('篮球场', 2000)
zp_house.add_fur(basketball_place)
